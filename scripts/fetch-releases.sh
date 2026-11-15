#!/usr/bin/env bash
# Writes the newest release of each program to data/releases/<repo>.json for the download tables: tag, date, page,
# and the archives with size and SHA-256. Uses GITHUB_TOKEN when it is set (CI), else the API without a token.
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p data/releases
auth=()
if [ -n "${GITHUB_TOKEN:-}" ]; then
  auth=(-H "Authorization: Bearer ${GITHUB_TOKEN}")
fi
for repo in freemapper freemapper-print freemapper-courseplan; do
  curl -fsSL ${auth[@]+"${auth[@]}"} -H "Accept: application/vnd.github+json" \
    -A "freemapper-site (+https://github.com/HenryJobst/freemapper-site)" \
    "https://api.github.com/repos/HenryJobst/${repo}/releases/latest" |
    jq '{tag: .tag_name, date: .published_at, url: .html_url,
         assets: [.assets[]
                  | select(.name | test("\\.(tar\\.gz|zip)$"))
                  | {name, size, url: .browser_download_url, sha256: (.digest // "" | sub("^sha256:"; ""))}]}' \
    > "data/releases/${repo}.json"
  echo "${repo}: $(jq -r .tag "data/releases/${repo}.json")"
done
