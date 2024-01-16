import csv
from pathlib import Path

# with open("standardlibrary/data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

path = Path("standardlibrary")
print(path)
with open(path / "data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader)) ## can't iterate twice, so if this is uncommented, the following rows won't work (15, 16)
    for row in reader:
        print(row)
