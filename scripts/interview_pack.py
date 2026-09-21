from pathlib import Path
import json,datetime
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/'career/job-search-config.json').read_text()); out=ROOT/'career/reports'; out.mkdir(parents=True,exist_ok=True)
questions=[{'role':role,'questions':['Describe a financial reporting problem you solved.','How do you validate a reconciliation?','How do you identify and mitigate financial control risks?','Describe your experience with budgets, forecasts, or grant financial management.']} for role in cfg['profile']['primary_roles']]
(out/'interview-pack.json').write_text(json.dumps({'generated':datetime.datetime.utcnow().isoformat()+'Z','packs':questions},indent=2),encoding='utf-8')
print('Interview pack generated.')
