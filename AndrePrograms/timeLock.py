############################################################################
# timeLock.py
#
# Python3 version: 3.6.8
# Run program:
#       python3 timeLock.py
#   OR  python3 < epoch.txt
#      where epoch.txt is any string with format: year month day hr min sec
#
# Note: must specify MANUAL_DATETIME or set it to False
#############################################################################

### LIBRARIES ###
from sys import stdin
from datetime import datetime, timedelta
import pytz
from hashlib import md5

### GLOBALS ###
# debug mode?
DEBUG = False

# set to True if on the challenge server
ON_SERVER = False

# valid time interval
INTERVAL = 60

# manual current datetime?
MANUAL_DATETIME = "2017 04 26 15 14 30"

if (MANUAL_DATETIME == False):
    current = datetime.now() # create an naive nowutc datetime object
else:
    # naive current datetime
    current = datetime.strptime(MANUAL_DATETIME, "%Y %m %d %H %M %S")

# Get the Epoch time
EPOCH_TIME = input()

epoch = datetime.strptime(EPOCH_TIME, "%Y %m %d %H %M %S")

########### Conversion to UTC using pytz #################
# local is the local timezone
local = pytz.timezone("America/Chicago")
# localize the epoch and current times then convert them to UTC
# note the epoch time is assumed to have occured in this local timezone
epoch_local = local.localize(epoch)
epoch_utc = epoch_local.astimezone(pytz.utc)
current_local = local.localize(current)
current_utc = current_local.astimezone(pytz.utc)

############ TIME DIFFERENCE IN SECONDS #################################
# compute difference in seconds between manual and epoch
time_diff = int((current_utc - epoch_utc).total_seconds())

# however we want the difference in seconds in the relevant 60 sec interval
# not sure how to incororate the  INTERVAL variable yet.
epoch_utc_sec = int(epoch_utc.strftime("%S")) # get the seconds of the epoch time
current_utc_sec = int(current_utc.strftime("%S"))

# We can dial the current time back one second until its seconds equal epoch's
current_utc_beg = current_utc # initalize equal to the current utc time
while(epoch_utc_sec != current_utc_sec):
    current_utc_beg = current_utc_beg - timedelta(seconds = 1)
    current_utc_sec = int(current_utc_beg.strftime("%S")) #int of seconds

time_diff2 = str(int((current_utc_beg - epoch_utc).total_seconds()) )

################# GET THE HASH value ##################################
# get a hash - > md5sum()
hash1 = md5(time_diff2.encode()).hexdigest()
hash2 = md5(hash1.encode()).hexdigest()
hash = str(hash2)
################# Get the code! ############################################
code = ""
alph = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
num_ctr = 0
alph_ctr = 0
for i in hash:
    if (i in alph):
        alph_ctr += 1
    if (i in num):
        num_ctr += 1
### account for three special cases:
## I could probably make this cleaner/mo efficient, but it works for now.
if (alph_ctr == 0 or alph_ctr == 1):
    for i in hash:
        if (i in alph):
            code += i
    for i in reversed(hash):
        if (len(code) < 4):
            if (i in num):
                code += i
        if (len(code) > 4):
            break
elif(num_ctr == 0):
    for i in hash:
        if (len(code) < 4):
            if (i in alph):
                code += i
elif(num_ctr == 1):
    for i in hash:
        if (len(code) < 2):
            if (i in alph):
                code += i
        if (len(code) > 2):
            for j in reversed(hash):
                if (j in num):
                    code += j
                if (len(code) > 3):
                    break
        if (len(code) > 3 and len(code) < 4):
            if (i in alph):
                code += i
        if (len(code) > 4):
            break
## This is the main part that will run except for the special cases.
else:
    ## From left to right pick the first two letters
    for i in hash:
        if (len(code) < 2):
            if (i in alph):
                code += i
        if (len(code) > 2):
            break
    ## From right to left pick the first two numbers (reversed() reverses hash)
    for i in reversed(hash):
        if (len(code) < 4):
            if (i in num):
                code += i
        if (len(code) > 4):
            break

### OUTPUT ###
if (DEBUG):
    print("Current (UTC): {}".format(current_utc) )
    print("Epoch (UTC): {}".format(epoch_utc) )
    print("Seconds: {}".format(time_diff) )
    print("Seconds: {}".format(time_diff2) )
    print("MD5 #1: {}".format(hash1) )
    print("MD5 #2: {}".format(hash2) )
    print("Code: {}".format(code) )
else:
    print(code)
