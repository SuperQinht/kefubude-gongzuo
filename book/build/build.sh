#!/bin/sh
# 用法：sh build.sh [输出文件名]
set -e
cd "$(dirname "$0")"
OUT=${1:-../output/毛泽东：在不确定中下判断.epub}
rm -rf norm && python3 normalize.py ../chapters norm
pandoc meta.yaml norm/*.md \
  -f markdown+fenced_divs+footnotes -t epub3 \
  --toc --toc-depth=3 --split-level=2 \
  --epub-cover-image=cover.jpg --css=epub.css \
  --metadata toc-title=目录 \
  -o "$OUT"
rm -rf norm
java -jar /usr/share/java/epubcheck.jar "$OUT" 2>&1 | tail -3
