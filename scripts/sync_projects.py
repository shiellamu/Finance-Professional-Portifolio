from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
projects=[]
for p in sorted(ROOT.iterdir()):
 if p.is_dir() and not p.name.startswith('.') and p.name not in {'career','config','scripts','setup-tools','docs','tests'}:
  readme=p/'README.md'; projects.append({'name':p.name,'readme':str(readme.relative_to(ROOT)) if readme.exists() else None})
(ROOT/'portfolio-projects.json').write_text(json.dumps(projects,indent=2),encoding='utf-8')
print(f'Indexed {len(projects)} portfolio areas.')
