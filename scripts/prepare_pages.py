"""Prepare the static site for either a GitHub project path or a custom domain."""
from pathlib import Path
import os
import re
import shutil

root = Path(__file__).resolve().parents[1]
out = root / '_site'
base = os.environ.get('PAGES_BASE_PATH', '').rstrip('/')
if base and (not base.startswith('/') or '..' in base or any(c in base for c in '\"\'<>')):
    raise ValueError('Invalid GitHub Pages base path')
shutil.copytree(root / 'dist', out, dirs_exist_ok=True)
for file in out.rglob('*.html'):
    html = file.read_text()
    html = re.sub(r'((?:href|src)=\")/(?!/)', lambda m: m[1] + base + '/', html)
    file.write_text(html)
(out / '.nojekyll').touch()
print('Prepared GitHub Pages output at', out)
