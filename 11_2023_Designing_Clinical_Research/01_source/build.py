"""Compile the Chinese text in a fresh temporary directory."""
from pathlib import Path
import argparse
import json
import os
import shutil
import subprocess
import tempfile

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-directory', type=Path)
    args = parser.parse_args()
    config = json.loads((SOURCE / 'build_config.json').read_text(encoding='utf-8'))
    complete = config['source_status'] == 'translated_tex'
    default = ROOT / ('00_books' if complete else 'work/designing_clinical_research')
    destination = (args.output_directory or default).resolve()
    if not complete and destination.is_relative_to((ROOT / '00_books').resolve()):
        raise SystemExit('Translation is incomplete; use a working directory for this build.')
    latexmk = shutil.which('latexmk')
    if not latexmk or not shutil.which(config['compiler']):
        raise SystemExit('latexmk and XeLaTeX are required; see README_build.txt.')
    work = Path(tempfile.mkdtemp(prefix='dcr_cn_')).resolve()
    source, build = work / 'source', work / 'build'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    build.mkdir()
    command = [latexmk, '-norc', '-xelatex', '-latexoption=-no-shell-escape',
               '-interaction=nonstopmode', '-halt-on-error', '-file-line-error',
               '-jobname=' + config['jobname'], '-outdir=' + str(build), config['main']]
    environment = os.environ.copy()
    environment['LC_ALL'] = environment['LANG'] = 'C'
    result = subprocess.run(command, cwd=source, env=environment,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / 'console.txt').write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-7000:])
        raise SystemExit('Build failed; inspect ' + str(work))
    log = (build / (config['jobname'] + '.log')).read_text(encoding='utf-8', errors='replace')
    for message in ('There were undefined references', 'There were undefined citations',
                    'There were multiply-defined labels', 'Missing character:'):
        if message in log:
            raise SystemExit(message + '; inspect ' + str(work))
    name = config['pdf_name'] if complete else 'designing_clinical_research_cn_in_progress.pdf'
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / name
    shutil.copyfile(build / (config['jobname'] + '.pdf'), target)
    print(json.dumps({'pdf': str(target), 'build_directory': str(work),
                      'translation_complete': complete}, ensure_ascii=False))


if __name__ == '__main__':
    main()
