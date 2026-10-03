#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ "${1:-}" == "--check-only" ]]; then
 for f in config/portfolio-config.json career/job-search-config.json career/ats-rules.json SECURITY.md .gitignore; do test -f "$ROOT/$f" || { echo "Missing $f"; exit 1; }; done
 echo 'Required configuration files present.'; exit 0
fi
echo 'Shiella portfolio setup'; echo 'Review portfolio config, career config, job sources, ATS rules, verified evidence, and GitHub settings.'; echo 'Then run ./verify-portfolio.sh'
