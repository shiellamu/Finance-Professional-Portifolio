from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
counts={}
for p in ROOT.rglob('*'):
 if p.is_file() and '.git' not in p.parts: counts[p.suffix or '[no extension]']=counts.get(p.suffix or '[no extension]',0)+1
print(json.dumps({'file_type_counts':counts},indent=2))
