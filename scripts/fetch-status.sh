#!/usr/bin/env bash
# Fetches the service status that the nightly run of freemapper keeps on its branch `status` (issue #286, ADR 0186)
# and writes data/status.json for the notice about known outages. Without a status (the branch does not exist yet,
# GitHub does not answer) the notice stays away: the file then holds no outage, and the build does not fail.
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p data
tmp=$(mktemp)
if curl -fsSL --max-time 30 -A "freemapper-site (+https://github.com/HenryJobst/freemapper-site)" \
  "https://raw.githubusercontent.com/HenryJobst/freemapper/status/status.json" -o "$tmp" &&
  jq -e '.down_by_adapter | type == "object"' "$tmp" >/dev/null; then
  mv "$tmp" data/status.json
else
  rm -f "$tmp"
  echo '{"updated": "", "services": {}, "down_by_adapter": {}}' >data/status.json
  echo "no service status; the notice stays away"
fi
echo "down: $(jq -r '.down_by_adapter | keys | join(", ")' data/status.json)"
