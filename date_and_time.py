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

short_date = now.strftime("%Y-%m-%d_%H:%M:%S")
print(short_date)
with open(f"right_now_{short_date}.txt", "w") as f:
    f.write(str(now))
