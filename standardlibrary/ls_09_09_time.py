import time
from datetime import datetime, timedelta

# https://docs.python.org/3/library/datetime.html


# times
def send_emails():
    for i in range(100000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)


# dates
dt = datetime(2024, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2024/01/15", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m/%d"))
dt2 = datetime(2025, 1, 1)
print(dt2 > dt)


# time delta
dt = datetime(2024, 1, 1)
duration = datetime.now() - dt
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total seconds", duration.total_seconds())

dt3 = datetime.now() + timedelta(days=1, seconds=1000)
print(dt3)
