#!/usr/bin/env bash
# Fetches the examples of freemapper (main branch: README tables and preview images, not the large files) and writes
# data/examples.json for the gallery and static/examples/<dir>/ with the preview images. The PDFs stay on GitHub.
set -euo pipefail

cd "$(dirname "$0")/.."
src=vendor/freemapper
rm -rf "$src" static/examples
git clone -q --depth 1 --filter=blob:none --sparse https://github.com/HenryJobst/freemapper "$src"
git -C "$src" sparse-checkout set --no-cone '/examples/README.md' '/examples/README.en.md' '/examples/international.md' '/examples/international.en.md' '/examples/*/preview.webp' \
  '/examples/*/preview-thumb.webp'
python3 scripts/examples.py "$src/examples" data/examples.json static/examples
