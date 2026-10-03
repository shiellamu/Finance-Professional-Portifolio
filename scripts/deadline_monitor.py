from pathlib import Path
import csv,datetime
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'career/application-schema.csv').open(encoding='utf-8')))
today=datetime.date.today()
print(f'Applications tracked: {len(rows)}')
for r in rows:
 d=r.get('deadline','')
 if d:
  try:
   deadline=datetime.date.fromisoformat(d)
   if deadline<today and r.get('status','').lower() not in {'submitted','closed','withdrawn'}: print('PAST DEADLINE:',r.get('company'),r.get('role'))
  except ValueError: print('INVALID DEADLINE:',d)
