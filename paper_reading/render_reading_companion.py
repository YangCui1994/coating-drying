#!/usr/bin/env python3

import argparse
import html
import re
from pathlib import Path

import markdown


CSS = """
@page { size: A4; margin: 15mm 14mm 16mm; }
* { box-sizing: border-box; }
body {
  max-width: 182mm;
  margin: 0 auto;
  color: #20262e;
  font-family: "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", Arial, sans-serif;
  font-size: 9.4pt;
  line-height: 1.58;
  letter-spacing: 0;
}
.cover {
  min-height: 255mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  break-after: page;
  border-top: 8px solid #0f5b67;
  padding: 24mm 10mm;
}
.cover h1 { margin: 0 0 12mm; color: #173e47; font-size: 27pt; line-height: 1.25; border: 0; }
.cover .source { font-size: 13pt; line-height: 1.45; color: #3e5961; margin-bottom: 8mm; }
.cover .meta { color: #61737a; font-size: 10.5pt; margin: 2mm 0; }
.cover .label { color: #0f5b67; font-weight: 700; margin-top: 15mm; }
h1 { color: #173e47; font-size: 21pt; line-height: 1.25; margin: 0 0 8mm; }
h2 {
  color: #0f5b67;
  font-size: 15.5pt;
  line-height: 1.3;
  margin: 11mm 0 4mm;
  padding-bottom: 2mm;
  border-bottom: 1.3px solid #8db6bc;
  break-after: avoid;
}
h2[id^="fig-"] { break-before: page; }
h3 { color: #76501d; font-size: 11.8pt; margin: 7mm 0 2.5mm; break-after: avoid; }
p { margin: 1.8mm 0; orphans: 3; widows: 3; }
blockquote {
  margin: 4mm 0;
  padding: 3mm 5mm;
  border-left: 4px solid #d28a2d;
  background: #f5f7f7;
  color: #46545a;
}
ul, ol { margin: 2mm 0; padding-left: 7mm; }
li { margin: 1mm 0; }
strong { color: #172f35; }
code { background: #edf1f2; padding: 0.2mm 0.8mm; border-radius: 2px; }
pre {
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  background: #f3f6f6;
  border: 1px solid #d5dfe1;
  padding: 4mm;
  font-size: 8.7pt;
  line-height: 1.45;
  break-inside: avoid;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 3mm 0 5mm;
  font-size: 7.8pt;
  line-height: 1.38;
}
thead { display: table-header-group; }
tr { break-inside: avoid; }
th {
  background: #173e47;
  color: white;
  text-align: left;
  padding: 2mm 1.8mm;
  border: 0.5px solid #315963;
}
td { vertical-align: top; padding: 1.7mm; border: 0.5px solid #bfcdd0; }
tbody tr:nth-child(even) { background: #f5f8f8; }
img {
  display: block;
  max-width: 100%;
  max-height: 238mm;
  width: auto;
  height: auto;
  margin: 4mm auto 6mm;
  break-inside: avoid;
  image-rendering: auto;
}
a { color: #0f5b67; text-decoration: none; }
hr { border: 0; border-top: 1px solid #bfcdd0; margin: 6mm 0; }
"""


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--title", required=True)
    parser.add_argument("--source-title", required=True)
    parser.add_argument("--doi", required=True)
    args = parser.parse_args()

    source = Path(args.input)
    body = markdown.markdown(
        strip_frontmatter(source.read_text(encoding="utf-8")),
        extensions=["tables", "fenced_code", "toc"],
        output_format="html5",
    )
    body = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.S)
    document = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>{html.escape(args.title)}</title><style>{CSS}</style></head>
<body>
<section class="cover">
  <h1>{html.escape(args.title)}</h1>
  <div class="source">{html.escape(args.source_title)}</div>
  <div class="meta">Nature Communications, 2026</div>
  <div class="meta">DOI: {html.escape(args.doi)}</div>
  <div class="label">专业伴读样板 v1</div>
</section>
{body}
</body>
</html>"""
    Path(args.output).write_text(document, encoding="utf-8")


if __name__ == "__main__":
    main()
