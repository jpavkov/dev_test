from pathlib import Path
from time import ctime
import shutil

path = Path("standardlibrary/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(ctime(path.stat().st_ctime))
path.read_bytes()
print(path.read_text())

# copy file
source = Path("standardlibrary/__init__.py")
target = Path("standardlibrary/text.txt")
target.write_text(source.read_text())

# or copy file like this:
shutil.copy(source, target)
