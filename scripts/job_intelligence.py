from pathlib import Path
import json,datetime
ROOT=Path(__file__).resolve().parents[1]
cfg=json.loads((ROOT/'career/job-search-config.json').read_text())
out=ROOT/'career/reports'; out.mkdir(parents=True,exist_ok=True)
report={'generated':datetime.datetime.utcnow().isoformat()+'Z','primary_roles':cfg['profile']['primary_roles'],'secondary_roles':cfg['profile']['secondary_roles'],'regions':cfg['profile']['regions'],'high_relevance_notification':cfg['matching']['notify_on_high_relevance']}
(out/'career-intelligence.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('Career intelligence configuration report generated.')
