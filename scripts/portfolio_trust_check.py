from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/'config/portfolio-config.json').read_text())
assert cfg['portfolio']['data_policy']=='synthetic_or_anonymized_only'
assert cfg['portfolio']['evidence_policy']=='verified_only'
for p in ROOT.rglob('*'):
 if p.is_file() and p.suffix.lower() in {'.md','.txt','.json','.csv','.html'}:
  s=p.read_text(errors='ignore')
  if re.search(r"(api[_ -]?key|secret|password)\s*[:=]\s*['\"]?[^\s'\"]{12,}",s,re.I): raise SystemExit(f'Potential credential assignment in {p}')
print('Trust/privacy policy checks passed.')
