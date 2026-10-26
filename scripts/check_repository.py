"""Check English paths, book layout, recorded hashes and Git LFS attributes.

Run from any directory. Use --include-local to include ignored working files.
This read-only check does not compile books or evaluate translation quality.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BOOK_DIRS = ('00_originals', '01_source', '02_glossary', '03_reviews', '05_references')
RUNTIME_DIRS = {'.git', '__pycache__', '.venv', 'venv', 'node_modules'}
ARCHIVE_SUFFIXES = ('.zip', '.tar', '.tar.gz', '.tgz', '.7z', '.rar')


def git(*args, input_bytes=None):
    return subprocess.run(['git', '-C', str(ROOT), *args], input=input_bytes,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout


def paths(include_local):
    if include_local:
        found = []
        for base, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in RUNTIME_DIRS]
            found.extend(Path(base, name) for name in dirs + files)
        return sorted(found)
    names = git('ls-files', '--cached', '--others', '--exclude-standard', '-z').decode('utf-8').split('\0')
    # During a rename, the index may still contain old paths. Check the live tree.
    return sorted({ROOT / name for name in names if name and (ROOT / name).exists()})


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--include-local', action='store_true')
    args = parser.parse_args()
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    def existing(relative):
        candidate = (ROOT / relative).resolve()
        valid = candidate.is_relative_to(ROOT) and candidate.exists()
        require(valid, 'Missing or outside repository: ' + relative)
        return candidate if valid else None

    def check_hash(relative, expected):
        candidate = existing(relative)
        if candidate and candidate.is_file():
            require(sha256(candidate) == expected, 'SHA-256 mismatch: ' + relative)

    entries = paths(args.include_local)
    for path in entries:
        require(path.relative_to(ROOT).as_posix().isascii(),
                'Non-ASCII path: ' + path.relative_to(ROOT).as_posix())
    # Syntax-check versioned/visible metadata, without interpreting historical claims.
    for path in paths(False):
        if path.suffix == '.json' and path.is_file():
            try:
                json.loads(path.read_text(encoding='utf-8-sig'))
            except (ValueError, UnicodeError) as exc:
                errors.append(f'Invalid JSON: {path.relative_to(ROOT)}: {exc}')

    manifest = json.loads((ROOT / '00_file_organization.json').read_text(encoding='utf-8'))
    require(tuple(manifest['subfolders']) == BOOK_DIRS, 'Book folder schema differs from manifest')
    expected_pdfs = set()
    for book in manifest['books']:
        folder = book['folder']
        for dirname in BOOK_DIRS:
            existing(folder + '/' + dirname)
        source = book['chinese_source']
        require(source == folder + '/01_source', 'Unexpected source location: ' + source)
        for name in ('build.py', 'build.ps1', 'build_config.json', 'README_build.txt', 'translation_style.md'):
            existing(source + '/' + name)
        config_path = existing(source + '/build_config.json')
        if config_path:
            config = json.loads(config_path.read_text(encoding='utf-8'))
            if config.get('source_status') == 'missing_chinese_tex':
                require(config.get('main') is None,
                        'Missing-source project must not declare a buildable main: ' + folder)
                require(book.get('chinese_source_status') == 'missing_chinese_tex',
                        'Missing Chinese source status differs from manifest: ' + folder)
            else:
                existing(source + '/' + config['main'])
            if config.get('index'):
                existing(source + '/' + config['index'])
            for alias in config.get('frozen_aliases', []):
                existing(source + '/' + alias['source'])
            require(book['translated_pdf'] == '00_books/' + config['pdf_name'],
                    'Build PDF name differs from manifest: ' + folder)
        check_hash(book['relative_path'], book['sha256'])
        check_hash(book['translated_pdf'], book['translated_sha256'])
        expected_pdfs.add(book['translated_pdf'])
        if book.get('tex_source'):
            existing(book['tex_source'])
            if book.get('tex_source_sha256'):
                check_hash(book['tex_source'], book['tex_source_sha256'])
        if book.get('split'):
            for name in book['split']['manifest']:
                existing(book['split']['output_dir'] + '/' + name)
    actual_pdfs = {p.relative_to(ROOT).as_posix() for p in (ROOT / '00_books').glob('*.pdf')}
    require(expected_pdfs == actual_pdfs, '00_books PDF files differ from manifest')
    require(manifest['collection_count'] == len(manifest['books']), 'Incorrect collection count')
    require(manifest['translated_pages_total'] == sum(b['translated_pages'] for b in manifest['books']),
            'Incorrect recorded page total')
    # Current navigation documents only. Historical review links may name old stages.
    docs = [ROOT / 'README.md', ROOT / 'AGENTS.md', *ROOT.glob('.agents/**/*.md')]
    for doc in docs:
        for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', doc.read_text(encoding='utf-8-sig')):
            href = unquote(href.strip('<>').split('#')[0])
            if not href or re.match(r'[a-zA-Z][\w+.-]*:', href):
                continue
            require((doc.parent / href).exists(), f'Broken link in {doc.relative_to(ROOT)}: {href}')

    lfs_files = [p.relative_to(ROOT).as_posix() for p in paths(False)
                 if p.is_file() and (p.suffix.lower() == '.pdf' or str(p).lower().endswith(ARCHIVE_SUFFIXES))]
    if lfs_files:
        attributes = git('check-attr', '-z', '--stdin', 'filter',
                         input_bytes=('\0'.join(lfs_files) + '\0').encode('utf-8')).decode('utf-8').split('\0')
        for index in range(0, len(attributes) - 1, 3):
            name, _, value = attributes[index:index + 3]
            require(value == 'lfs', 'Missing Git LFS attribute: ' + name)
    for error in errors:
        print('ERROR: ' + error, file=sys.stderr)
    print(json.dumps({'status': 'failed' if errors else 'passed', 'paths_checked': len(entries),
                      'books': len(manifest['books']), 'lfs_files': len(lfs_files),
                      'include_local': args.include_local, 'errors': len(errors)}, ensure_ascii=False))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
