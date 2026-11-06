"""Build the Chinese TeX in a fresh temporary directory."""
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
    parser.add_argument("--output-directory", type=Path)
    args = parser.parse_args()
    config = json.loads((SOURCE / "build_config.json").read_text(encoding="utf-8"))
    complete = config["source_status"] == "translated_tex"
    collection = (ROOT / "00_books").resolve()
    preview = ROOT / "work" / "mathematical_foundations_of_ai_manifold"
    destination = (args.output_directory or (collection if complete else preview)).resolve()
    if not complete and destination.is_relative_to(collection):
        raise SystemExit("The translation is in progress. Choose a working directory for the PDF.")

    latexmk = shutil.which("latexmk")
    if not latexmk or not shutil.which(config["compiler"]):
        raise SystemExit("Install latexmk and XeLaTeX. See README_build.txt.")

    work = Path(tempfile.mkdtemp(prefix="manifold_cn_"))
    source = work / "source"
    output = work / "build"
    shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    output.mkdir()
    (source / "translation_status.tex").write_text(
        "\\translationcompletetrue\n" if complete else "\\translationcompletefalse\n",
        encoding="ascii",
    )
    jobname = config["jobname"]
    command = [
        latexmk, "-norc", "-xelatex", "-e", "$max_repeat = 6;",
        "-latexoption=-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", "-jobname=" + jobname, "-outdir=" + str(output), config["main"],
    ]
    environment = os.environ.copy()
    environment["LC_ALL"] = environment["LANG"] = "C"
    result = subprocess.run(
        command, cwd=source, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    (work / "console.txt").write_bytes(result.stdout)
    if result.returncode:
        print(result.stdout.decode("utf-8", errors="replace")[-6000:])
        raise SystemExit("Build failed. See " + str(work))

    log = (output / f"{jobname}.log").read_text(encoding="utf-8", errors="replace")
    warnings = ["Missing character:", "There were multiply-defined labels"]
    if complete:
        warnings.extend(["There were undefined references", "There were undefined citations"])
    for warning in warnings:
        if warning in log:
            raise SystemExit(warning + " See " + str(work))

    destination.mkdir(parents=True, exist_ok=True)
    target = destination / (config["pdf_name"] if complete else f"{jobname}_in_progress.pdf")
    with tempfile.NamedTemporaryFile(dir=destination, suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
    try:
        shutil.copyfile(output / f"{jobname}.pdf", temporary)
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({"pdf": str(target), "build_directory": str(work),
                      "translation_complete": complete}, ensure_ascii=False))


if __name__ == "__main__":
    main()
