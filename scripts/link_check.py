from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
bad=[]
for p in ROOT.rglob('*.md'):
 text=p.read_text(errors='ignore')
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
  if target.startswith(('#','http://','https://','mailto:')): continue
  if not (p.parent/target.split('#')[0]).resolve().exists(): bad.append((str(p.relative_to(ROOT)),target))
if bad:
 for item in bad: print('BROKEN:',item)
 raise SystemExit(1)
print('No broken local Markdown links detected.')
