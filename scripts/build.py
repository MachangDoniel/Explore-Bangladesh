from pathlib import Path
import shutil
root = Path(__file__).resolve().parent.parent
shutil.copytree(root / 'public', root / 'dist', dirs_exist_ok=True)
print('Built static website in dist/')
