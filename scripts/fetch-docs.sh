#!/usr/bin/env bash
# Fetches the manuals and changelogs of the three programs at their newest release tags (data/releases, written by
# fetch-releases.sh) and turns them into content/handbuch/<repo>/, content/aenderungen/<repo>.md and
# static/handbuch-bilder/<repo>/.
set -euo pipefail

cd "$(dirname "$0")/.."
for repo in freemapper freemapper-print freemapper-courseplan; do
  tag=$(jq -r .tag "data/releases/${repo}.json")
  src="vendor/docs/${repo}"
  rm -rf "$src" "content/handbuch/${repo}" "static/handbuch-bilder/${repo}"
  git clone -q --depth 1 --branch "$tag" --filter=blob:none --sparse "https://github.com/HenryJobst/${repo}" "$src" 2>/dev/null
  git -C "$src" sparse-checkout set --no-cone '/docs/manual/' '/CHANGELOG.md' '/CHANGELOG.en.md'
  python3 scripts/docs.py "$src" "$repo" "$tag" content static
done
