"""Build the imported Chinese edition with XeLaTeX and Biber in a temporary directory."""
from pathlib import Path
import argparse
import json
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-directory', type=Path, default=ROOT.parent.parent / '00_books')
    parser.add_argument('--keep-work', action='store_true', help='Keep temporary compiler files.')
    args = parser.parse_args()
    config = json.loads((ROOT / 'build_config.json').read_text(encoding='utf-8'))
    programs = {name: shutil.which(name) for name in ('latexmk', config['compiler'], config['bibliography'])}
    missing = [name for name, path in programs.items() if not path]
    if missing:
        raise SystemExit('Required programs not found in PATH: ' + ', '.join(missing))

    work = Path(tempfile.mkdtemp(prefix='cn_book_')).resolve()
    source, build = work / 'source', work / 'build'
    shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns('__pycache__', 'build', '*.pyc'))
    build.mkdir()
    for directory in source.rglob('*'):
        if directory.is_dir():
            (build / directory.relative_to(source)).mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env['BIBINPUTS'] = str(source) + os.pathsep
    # Perl tools on Windows need a locale accepted by the installed runtime.
    if os.name == 'nt':
        env['LC_ALL'] = 'C'
        env['LANG'] = 'C'
    command = [programs['latexmk'], '-norc', '-' + config['compiler'],
               '-latexoption=-no-shell-escape', '-interaction=nonstopmode',
               '-halt-on-error', '-file-line-error', '-jobname=' + config['jobname'],
               '-outdir=' + str(build), config['main']]
    result = subprocess.run(command, cwd=source, env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / 'console.txt').write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-5000:])
        raise SystemExit('Build failed; compiler files retained at ' + str(work))
    log = (build / (config['jobname'] + '.log')).read_text(encoding='utf-8', errors='replace')
    if any(message in log for message in ('There were undefined references',
                                          'There were undefined citations', 'Missing character:')):
        raise SystemExit('Unresolved references or missing characters; inspect ' + str(work))
    output = args.output_directory.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / config['pdf_name']
    shutil.copyfile(build / (config['jobname'] + '.pdf'), destination)
    print(json.dumps({'pdf': str(destination), 'temporary_directory': str(work),
                      'temporary_files_kept': args.keep_work}, ensure_ascii=False))
    if not args.keep_work:
        if work.parent == Path(tempfile.gettempdir()).resolve() and work.name.startswith('cn_book_'):
            shutil.rmtree(work)


if __name__ == '__main__':
    main()
