# https://sqlitebrowser.org/

import sqlite3
import json
from pathlib import Path
path = Path("standardlibrary")

# movies = json.loads(Path("standardlibrary/movies.json").read_text())

# movies = json.loads((path / "movies.json").read_text())
# print(movies)

# write data
# with sqlite3.connect(path / "db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES (?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()


# read data
with sqlite3.connect(path / "db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)

    # this does the same as below:
    # for row in cursor:
    #     print(row)

    # does the same as above
    movies = cursor.fetchall()
    print(movies)
