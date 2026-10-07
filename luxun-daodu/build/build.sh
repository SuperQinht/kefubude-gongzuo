#!/bin/sh
set -e
cd "$(dirname "$0")"
rm -rf norm && python3 normalize.py ../chapters norm
pandoc meta.yaml 000-front.md norm/0*.md \
  -f markdown+fenced_divs -t epub3 \
  --toc --toc-depth=2 --split-level=1 \
  --epub-cover-image=cover.jpg --css=epub.css \
  -o ../铁屋与路-鲁迅名篇历史导读.epub
rm -rf norm
echo built
