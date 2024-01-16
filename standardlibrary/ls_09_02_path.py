from pathlib import Path

# https://docs.python.org/3/library/pathlib.html
# Path("/usr/local/bin")
# Path() # current folder
# Path() / "ecommerce" / "__init__.py"

path = Path("ecommerce/__init__.py")

path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
path = path.with_suffix(".txt")
print(path)
