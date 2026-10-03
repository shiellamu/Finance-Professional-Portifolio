from pathlib import Path
import csv, json
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'career/application-schema.csv').open(encoding='utf-8')))
out=ROOT/'career/reports'; out.mkdir(parents=True,exist_ok=True)
(out/'application-summary.json').write_text(json.dumps({'tracked_applications':len(rows),'statuses':sorted({r.get('status','') for r in rows if r.get('status')})},indent=2),encoding='utf-8')
print(f'Tracked applications: {len(rows)}')
