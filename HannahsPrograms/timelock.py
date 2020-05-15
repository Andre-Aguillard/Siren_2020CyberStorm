# Hannah Folkertsma
# CSC 442 - 002
# May 8, 2020
# Program 5: Timelock
# Python 2
#----------------------------------------------------------------------------------------
from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

DEBUG = False
USE_MANUAL = False
ON_SERVER = False
INTERVAL = 60
if USE_MANUAL:
    MANUAL_DATETIME = "2017 03 23 18 02 06"
epoch  = stdin.read()

# calculate seconds elapsed from epoch to current system time
systemtime = datetime.now()
local_time = pytz.timezone("America/Chicago")
if USE_MANUAL:
    current_naive = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")
else:
    current_naive = systemtime
epoch_naive = datetime.strptime(epoch, "%Y %m %d %H %M %S")
current_local = local_time.localize(current_naive, is_dst=None)
epoch_local = local_time.localize(epoch_naive, is_dst=None)
current_utc = current_local.astimezone(pytz.utc)
epoch_utc = epoch_local.astimezone(pytz.utc)

difference = (current_utc - epoch_utc).total_seconds()
difference = int(difference - difference % 60)
# hash using md5
hashresult = md5(str(difference).encode()).hexdigest()
hashresult = md5(hashresult.encode()).hexdigest()

if(DEBUG):
    print(hashresult)

# extract and concatenate the first 2 letters
count = 0
finalcode = ""
for char in hashresult:
    if char in "abcdefghijklmnopqrstuvwxyz":
        finalcode += char
        count += 1
        if count == 2:
          break

# going backwards, extract and concatenate the first 2 integers
count = 0
for i in range(1,len(hashresult)):
    char = hashresult[-i]
    if char in "0123456789":
        finalcode += char
        count += 1
        if count == 2:
            break
finalcode += hashresult[-1]

print(finalcode)
