"""Build the Chinese article in a fresh temporary directory."""
from pathlib import Path
import argparse
import json
import os
import shutil
import subprocess
import tempfile

SOURCE = Path(__file__).resolve().parent
REPOSITORY = SOURCE.parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-directory', type=Path, default=REPOSITORY / '00_books')
    parser.add_argument('--keep-work', action='store_true')
    args = parser.parse_args()
    config = json.loads((SOURCE / 'build_config.json').read_text(encoding='utf-8'))
    programs = {name: shutil.which(name) for name in ('latexmk', config['compiler'], config['bibliography'])}
    missing = [name for name, path in programs.items() if not path]
    if missing:
        raise SystemExit('Required programs not found in PATH: ' + ', '.join(missing))
    work = Path(tempfile.mkdtemp(prefix='wm_cn_')).resolve()
    source, build = work / 'source', work / 'build'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    build.mkdir()
    environment = os.environ.copy()
    environment['LC_ALL'] = environment['LANG'] = 'C'
    environment['BIBINPUTS'] = str(source) + os.pathsep
    command = [programs['latexmk'], '-norc', '-' + config['compiler'],
               '-latexoption=-no-shell-escape', '-interaction=nonstopmode',
               '-halt-on-error', '-file-line-error', '-jobname=' + config['jobname'],
               '-outdir=' + str(build), config['main']]
    result = subprocess.run(command, cwd=source, env=environment,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / 'console.txt').write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-6000:])
        raise SystemExit('Build failed; files retained at ' + str(work))
    log = (build / (config['jobname'] + '.log')).read_text(encoding='utf-8', errors='replace')
    if any(message in log for message in ('There were undefined references',
                                          'There were undefined citations', 'Missing character:')):
        raise SystemExit('Unresolved references or missing characters; inspect ' + str(work))
    destination = args.output_directory.expanduser().resolve() / config['pdf_name']
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(build / (config['jobname'] + '.pdf'), destination)
    print(json.dumps({'pdf': str(destination), 'temporary_directory': str(work),
                      'temporary_files_kept': args.keep_work}, ensure_ascii=False))
    if not args.keep_work:
        if work.parent == Path(tempfile.gettempdir()).resolve() and work.name.startswith('wm_cn_'):
            shutil.rmtree(work)


if __name__ == '__main__':
    main()
