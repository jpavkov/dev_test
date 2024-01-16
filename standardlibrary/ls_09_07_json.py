import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "Year": 1984},
    {"id": 2, "title": "Kindergarden Cop", "Year": 1990}
]

path = Path("standardlibrary")
data = json.dumps(movies)
# print(data)
# Path(Path("standardlibrary") / "movies.json").write_text(data)
Path(path / "movies.json").write_text(data)

data = Path(path / "movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[1]["title"])
