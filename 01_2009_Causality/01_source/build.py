"""Build the complete Chinese edition without writing temporary files into its source tree."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent

def state(folder):
    h = hashlib.sha256()
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix in {'.aux', '.toc', '.out', '.idx', '.brf'}:
            h.update(p.relative_to(folder).as_posix().encode())
            h.update(p.read_bytes())
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-directory', type=Path, default=ROOT.parent.parent / '00_books')
    parser.add_argument('--keep-work', action='store_true', help='Keep the temporary build directory for diagnosis.')
    args = parser.parse_args()
    config = json.loads((ROOT / 'build_config.json').read_text(encoding='utf-8'))
    engine = shutil.which('xelatex')
    if not engine:
        raise SystemExit('XeLaTeX was not found. Install TeX Live and add its binary directory to PATH.')
    work = Path(tempfile.mkdtemp(prefix='cn_book_')).resolve()
    src, build = work / 'source', work / 'build'
    shutil.copytree(ROOT, src, ignore=shutil.ignore_patterns('__pycache__', 'build', '*.pyc'))
    build.mkdir()
    for p in src.rglob('*'):
        if p.is_dir():
            (build / p.relative_to(src)).mkdir(parents=True, exist_ok=True)
    for alias in config.get('frozen_aliases', []):
        target = src / alias['target']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src / alias['source'], target)
        if target.suffix == '.bbl':
            copy = build / alias['target']
            copy.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(target, copy)
    env = os.environ.copy()
    env['BIBINPUTS'] = str(src) + os.pathsep
    env['BSTINPUTS'] = str(src) + os.pathsep
    job = config['jobname']
    run_count = 0
    def run(command, cwd):
        nonlocal run_count
        run_count += 1
        r = subprocess.run(command, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (work / ('console_%02d.txt' % run_count)).write_bytes(r.stdout)
        if r.returncode:
            print(r.stdout.decode('utf-8', errors='replace')[-5000:])
            raise RuntimeError('Build failed; diagnostic files retained at ' + str(work))
    def latex():
        run([engine, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
             '-jobname=' + job, '-output-directory=' + str(build), config['main']], src)
    latex()
    if config.get('bibtex'):
        bibtex = shutil.which('bibtex')
        if not bibtex:
            raise RuntimeError('BibTeX is required.')
        run([bibtex, job], build)
    stable = False
    for pass_number in range(2, 8):
        before = state(build)
        if config.get('index') and pass_number >= 3:
            indexer = shutil.which('upmendex')
            if not indexer:
                raise RuntimeError('upmendex is required.')
            run([indexer, '-q', '-s', str(src / config['index']), job + '.idx'], build)
        latex()
        if pass_number >= (4 if config.get('index') else 3) and before == state(build):
            stable = True
            break
    if not stable:
        raise RuntimeError('Pagination did not stabilize; inspect ' + str(work))
    log = (build / (job + '.log')).read_text(encoding='utf-8', errors='replace')
    fatal = ['There were undefined references', 'There were undefined citations', 'Missing character:']
    if any(s in log for s in fatal):
        raise RuntimeError('Unresolved references or missing characters; inspect ' + str(work))
    output = args.output_directory.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / config['pdf_name']
    shutil.copyfile(build / (job + '.pdf'), destination)
    print(json.dumps({'pdf': str(destination), 'passes': pass_number, 'pagination_stable': stable,
                      'temporary_directory': str(work), 'temporary_files_kept': args.keep_work}, ensure_ascii=False))
    if not args.keep_work:
        # The only recursive deletion is the unique directory allocated by tempfile above.
        if work.parent == Path(tempfile.gettempdir()).resolve() and work.name.startswith('cn_book_'):
            shutil.rmtree(work)

if __name__ == '__main__':
    main()
