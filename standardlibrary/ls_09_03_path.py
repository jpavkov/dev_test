from pathlib import Path

path = Path()

# path = Path("ecommerce")
# print(path)
# path.exists
# path.mkdir
# path.rmdir()
# path.rename("ecommerce2")

print(path.iterdir)
for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir()]
print(paths)

py_files = [p for p in path.rglob("*.py")]
print(py_files)
