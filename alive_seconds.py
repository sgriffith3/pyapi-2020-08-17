import time
import datetime


# Determine number of seconds we have been alive

today = datetime.datetime.now()

zeroth_bday = today.replace(year=1990, month=6, day=23)
print(today)
print(zeroth_bday)

diff = today - zeroth_bday
print(diff)
#diff_secs = diff.days * 60 * 60 * 24
#print(diff_secs)
print(diff.total_seconds())

#print(time.time())
