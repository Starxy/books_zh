"""Build the Chinese edition or one chapter from a fresh copy of the sources."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-directory', type=Path)
    parser.add_argument('--chapter', type=int, choices=range(1, 15))
    args = parser.parse_args()

    config = json.loads((SOURCE / 'build_config.json').read_text(encoding='utf-8'))
    chapter = args.chapter
    complete = config['source_status'] == 'translated_tex' and chapter is None
    collection = ROOT / '00_books'
    preview = ROOT / 'work' / 'efficient_llm_inference'
    destination = (args.output_directory or (collection if complete else preview)).resolve()
    if not complete and destination.is_relative_to(collection.resolve()):
        raise SystemExit('Build chapter previews and in-progress translations outside 00_books.')
    latexmk = shutil.which('latexmk')
    if not latexmk or not shutil.which(config['compiler']):
        raise SystemExit('Install latexmk and XeLaTeX. See README_build.txt.')

    work = Path(tempfile.mkdtemp(prefix='efficient_llm_inference_'))
    source = work / 'source'
    output = work / 'build'
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    output.mkdir()
    entry = config['main']
    jobname = config['jobname']
    pdf_name = config['pdf_name'] if complete else f'{jobname}_in_progress.pdf'
    if chapter is not None:
        jobname = f'ch{chapter:02d}_preview'
        pdf_name = f'{jobname}.pdf'
        entry = 'chapter_preview.tex'
        (source / entry).write_text(
            '\\input{layout}\n\\begin{document}\n'
            f'\\setcounter{{chapter}}{{{chapter - 1}}}\n'
            f'\\input{{chapters/ch{chapter:02d}}}\n\\end{{document}}\n',
            encoding='ascii',
        )

    command = [
        latexmk, '-norc', '-xelatex', '-e', '$max_repeat = 6;',
        '-latexoption=-no-shell-escape', '-interaction=nonstopmode',
        '-halt-on-error', '-file-line-error', '-jobname=' + jobname,
        '-outdir=' + str(output), entry,
    ]
    print(f'Build directory: {work}', flush=True)
    result = subprocess.run(command, cwd=source, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (work / 'console.txt').write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace')[-6000:])
        raise SystemExit('Compilation failed. See the build directory.')
    log = (output / f'{jobname}.log').read_text(encoding='utf-8', errors='replace')
    for warning in (
        'There were undefined references',
        'There were undefined citations',
        'There were multiply-defined labels',
        'Missing character:',
    ):
        if warning in log:
            raise SystemExit(warning + ' See the build directory.')

    destination.mkdir(parents=True, exist_ok=True)
    target = destination / pdf_name
    # Build and copy first so a failed attempt cannot overwrite an existing PDF.
    with tempfile.NamedTemporaryFile(dir=destination, suffix='.tmp', delete=False) as stream:
        temporary = Path(stream.name)
    try:
        shutil.copyfile(output / f'{jobname}.pdf', temporary)
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'PDF: {target}')


if __name__ == '__main__':
    main()
