"""Inventory a PDF for translation; optionally extract page-marked text and render pages."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


def page_list(value: str) -> list[int]:
    try:
        pages = sorted(set(int(part.strip()) for part in value.split(',')))
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Use comma-separated, one-based page numbers.') from exc
    if not pages or pages[0] < 1:
        raise argparse.ArgumentTypeError('Page numbers must be positive.')
    return pages


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--out-dir', required=True, type=Path, help='New or empty evidence directory.')
    parser.add_argument('--start', type=int, default=1, help='First PDF page to inspect (one-based).')
    parser.add_argument('--end', type=int, help='Last PDF page to inspect, inclusive; default: last page.')
    parser.add_argument('--extract-text', action='store_true', help='Save raw text with source PDF page markers.')
    parser.add_argument('--render-pages', type=page_list, default=[], help='Selected PDF pages, e.g. 1,12,30.')
    parser.add_argument('--dpi', type=int, default=160, help='Resolution for requested page renders.')
    args = parser.parse_args()
    try:
        import pymupdf
    except ImportError:
        parser.error('PyMuPDF is required: install the pymupdf package in the Python environment you use.')

    source = args.pdf.expanduser().resolve()
    output = args.out_dir.expanduser().resolve()
    if not source.is_file():
        parser.error('The source PDF does not exist.')
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        parser.error('The output directory must be new or empty; choose a separate directory for this run.')
    if args.dpi < 36 or args.dpi > 600:
        parser.error('--dpi must be between 36 and 600.')

    with pymupdf.open(source) as document:
        if not document.is_pdf:
            parser.error('The input must be a PDF.')
        if document.needs_pass:
            parser.error('This PDF requires a password; supply an accessible copy before inspection.')
        last = len(document) if args.end is None else args.end
        if not 1 <= args.start <= last <= len(document):
            parser.error('--start and --end must define a non-empty range inside this PDF.')
        if any(page < args.start or page > last for page in args.render_pages):
            parser.error('Every --render-pages entry must be inside the selected page range.')

        output.mkdir(parents=True, exist_ok=True)
        records = []
        extracted = []
        for number in range(args.start, last + 1):
            page = document[number - 1]
            text = page.get_text('text')
            controls = Counter(
                f'U+{ord(char):04X}' for char in text
                if (ord(char) < 32 and char not in '\n\r\t') or ord(char) == 127
            )
            record = {
                'pdf_page': number,
                'printed_label': page.get_label(),
                'width_pt': round(page.rect.width, 3),
                'height_pt': round(page.rect.height, 3),
                'text_characters_without_whitespace': len(''.join(text.split())),
                'suspicious_controls': dict(controls),
            }
            if args.extract_text:
                extracted.append(f'<<<PDFPAGE {number}>>>\n{text}\n')
            if number in args.render_pages:
                filename = f'page-{number:04d}.png'
                page.get_pixmap(dpi=args.dpi, alpha=False, annots=False).save(output / filename)
                record['render'] = filename
            records.append(record)

        inventory = {
            'schema_version': 1,
            'source_pdf': str(source),
            'source_sha256': sha256(source),
            'pdf_pages_total': len(document),
            'inspected_range': [args.start, last],
            'metadata': document.metadata,
            'bookmarks': document.get_toc(simple=True),
            'page_label_rules': document.get_page_labels(),
            'pages': records,
            'low_text_pages': [p['pdf_page'] for p in records if p['text_characters_without_whitespace'] < 60],
            'pages_with_suspicious_controls': [p['pdf_page'] for p in records if p['suspicious_controls']],
            'render_dpi': args.dpi if args.render_pages else None,
            'annotations_rendered': False,
            'interpretation': [
                'Low text may indicate scans, figures, title pages, or blank pages; inspect visually.',
                'Bookmarks and metadata are evidence, not an authoritative edition or section plan.',
                'Text is raw: no automatic OCR, reading-order repair, dehyphenation, or control-character mapping.',
                'Successful inspection does not establish translation completeness or correctness.',
            ],
        }
        if args.extract_text:
            (output / 'extracted_pages.txt').write_text(''.join(extracted), encoding='utf-8')
        (output / 'source_inventory.json').write_text(
            json.dumps(inventory, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
        )
    print(json.dumps({
        'inventory': str(output / 'source_inventory.json'),
        'inspected_pages': len(records),
        'rendered_pages': args.render_pages,
        'source_sha256': inventory['source_sha256'],
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
