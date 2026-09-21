from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/'career/job-search-config.json').read_text()); out=ROOT/'career/reports'; out.mkdir(parents=True,exist_ok=True)
(out/'tailoring-brief.md').write_text('# Resume Tailoring Brief\n\nUse only verified experience and qualifications.\n\n## Priority keywords\n\n'+'\n'.join(f'- {k}' for k in cfg['profile']['keywords'])+'\n',encoding='utf-8')
print('Tailoring brief generated.')
