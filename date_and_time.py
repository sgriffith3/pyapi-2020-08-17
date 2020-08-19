import time
import datetime

def sleepy(t):
    print(f"Sleeping for {t} seconds")
    time.sleep(t)
    print(f"Time to wake up!")


#sleepy(5)

now = datetime.datetime.now()
print(f"Right now it is {now}")

days_ago = 7
yesterday = now - datetime.timedelta(days=days_ago, hours=7)
print(f"{days_ago} days ago was {yesterday}")
tz_offset = datetime.timedelta(hours=4)
now = now - tz_offset
short_date = now.strftime("%Y-%m-%d_%H:%M:%S")
print(short_date)
with open(f"right_now_{short_date}.time.txt", "w") as f:
    f.write(str(now))



uptime = 12345678

def get_up(t):
    right_now = datetime.datetime.now()
    up_time = right_now - datetime.timedelta(seconds=t)
    print(up_time)
    total = right_now - up_time
    print(total)

get_up(uptime)
