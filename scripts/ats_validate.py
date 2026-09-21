from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/'career/ats-rules.json').read_text())
for key in ['document','content','checks']: assert key in cfg,f'Missing ATS config: {key}'
assert cfg['content']['never_add_unverified_claims'] is True
print('ATS configuration validation passed.')
