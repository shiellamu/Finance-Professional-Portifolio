from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'career/application-schema.csv'
rows=list(csv.DictReader(p.open(encoding='utf-8')))
seen=[]; out=[]
for r in rows:
 key=(r.get('company','').strip().lower(),r.get('role','').strip().lower(),r.get('location','').strip().lower())
 if key in seen: continue
 seen.append(key); out.append(r)
fields=list(rows[0].keys()) if rows else 'job_id company role location region source_url date_found deadline status relevance_score resume_version cover_letter_version ats_status notes'.split()
with p.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(out)
print(f'Deduplicated {len(rows)-len(out)} application rows.')
