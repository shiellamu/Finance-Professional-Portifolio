#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
required=("README.md" "SECURITY.md" ".gitignore" "config/portfolio-config.json" "career/job-search-config.json" "career/ats-rules.json" "career/job-sources.json" "career/application-schema.csv")
for f in "${required[@]}"; do test -f "$ROOT/$f" || { echo "Missing $f"; exit 1; }; done
python -m json.tool "$ROOT/config/portfolio-config.json" >/dev/null
python -m json.tool "$ROOT/career/job-search-config.json" >/dev/null
python -m json.tool "$ROOT/career/ats-rules.json" >/dev/null
python -m json.tool "$ROOT/career/job-sources.json" >/dev/null
echo "Portfolio verification passed."
