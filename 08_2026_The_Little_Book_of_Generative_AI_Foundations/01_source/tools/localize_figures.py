"""Replace figure prose with Chinese, retaining original paths and mathematical labels.

Input must be the extracted English TeX archive. Normal book builds use the
resulting figure PDFs and do not require PyMuPDF or this conversion step.
"""
from pathlib import Path
import argparse
import json
import pymupdf

SOURCE = Path(__file__).resolve().parents[1]
pymupdf.TOOLS.set_small_glyph_heights(True)


def localize(source, destination, replacements, font_path):
    doc = pymupdf.open(source)
    if len(doc) != 1:
        raise ValueError(f'Expected a one-page figure: {source}')
    page = doc[0]
    # The original Matplotlib exports crop these axis labels at the page edge.
    if source.name.startswith('fig1_4'):
        page.set_mediabox(pymupdf.Rect(0, 0, page.rect.width + 12, page.rect.height))
    elif source.name == 'fig2_3d_posterior.pdf':
        page.set_mediabox(pymupdf.Rect(-8, 0, page.rect.width, page.rect.height))
    font = pymupdf.Font(fontfile=str(font_path))
    lines = [line for b in page.get_text('dict')['blocks'] for line in b.get('lines', [])]
    pending, occupied = [], []
    for english, chinese in sorted(replacements.items(), key=lambda x: -len(x[0])):
        matches = page.search_for(english, flags=3)
        if not matches:
            raise ValueError(f'Text not found in {source.name}: {english!r}')
        accepted = 0
        for rect in matches:
            line = max(lines, key=lambda line: (pymupdf.Rect(line['bbox']) & rect).get_area())
            spans = [s for s in line['spans'] if (pymupdf.Rect(s['bbox']) & rect).get_area() > 0]
            size = max(s['size'] for s in spans)
            direction = line['dir']
            if abs(direction[0] - 1) < .01:
                rotate, available = 0, rect.width
                baseline = max(s['origin'][1] for s in spans)
                erase = pymupdf.Rect(rect.x0, baseline - .45 * size,
                                     rect.x1, baseline - .35 * size)
            elif abs(direction[1] + 1) < .01:
                rotate, available = 90, rect.height
                baseline = max(s['origin'][0] for s in spans)
                erase = pymupdf.Rect(baseline - .45 * size, rect.y0,
                                     baseline - .35 * size, rect.y1)
            else:
                raise ValueError(f'Unexpected text angle: {source.name}, {english}')
            # Type 3 font boxes can overlap adjacent lines. Compare and erase
            # within each line's central ink band, rather than the full box.
            if any((erase & previous).get_area() > erase.get_area() * .5 for previous in occupied):
                continue
            original_size = size
            width = font.text_length(chinese, fontsize=size)
            if width > available:
                size *= available / width
                width = available
            if size < original_size * .65:
                raise ValueError(f'Chinese label would be too small: {source.name}, {english}, {size}')
            if rotate == 0:
                point = (rect.x0 + (rect.width - width) / 2, baseline)
            else:
                point = (baseline, rect.y1 - (rect.height - width) / 2)
            # No fill and no drawing/image redaction: plotted data and arrows survive.
            page.add_redact_annot(erase, fill=False, cross_out=False)
            pending.append((point, chinese, size, rotate, rect))
            occupied.append(erase)
            accepted += 1
        if not accepted:
            raise ValueError(f'All matches overlapped another label: {source.name}, {english!r}')
    page.apply_redactions(images=0, graphics=0, text=0)
    for point, chinese, size, rotate, _ in pending:
        page.insert_text(point, chinese, fontname='ChineseLabels', fontfile=str(font_path),
                         fontsize=size, rotate=rotate, color=(0, 0, 0))
    # MuPDF's subsetter can omit a visible Latin glyph in mixed CJK labels.
    # fontTools retains the glyphs used by these figures (including panel c).
    doc.subset_fonts(fallback=True)
    destination.parent.mkdir(parents=True, exist_ok=True)
    doc.save(destination, garbage=4, deflate=True)
    doc.close()
    return len(pending)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--english-source', type=Path, required=True)
    parser.add_argument('--output-directory', type=Path, required=True)
    parser.add_argument('--font', type=Path, required=True, help='NotoSansCJKsc-Regular.otf')
    args = parser.parse_args()
    english_root = args.english_source.resolve() / 'figures'
    output = args.output_directory.resolve()
    if output == english_root or english_root in output.parents:
        raise SystemExit('Output must not overwrite or be placed inside the English source.')
    labels = json.loads((SOURCE / 'figures/labels_zh.json').read_text(encoding='utf8'))
    for filename, replacements in labels.items():
        candidates = list(english_root.rglob(filename))
        if len(candidates) != 1:
            raise ValueError(f'Expected one original file for {filename}: {candidates}')
        original = candidates[0]
        destination = output / original.relative_to(english_root)
        count = localize(original, destination, replacements, args.font)
        print(f'{filename}: {count} labels', flush=True)


if __name__ == '__main__':
    main()
