# Hannah Folkertsma
# CSC 442 - 002
# April 24, 2020
# Program 4: Chat (Timing) Covert Channel
#---------------------------------------------------------------------------
import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = True

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
covert_bin = ""
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
        # output the data
        stdout.write(data)
        stdout.flush()
        # start the "timer", get more data, and end the "timer"
        t0 = time()
        data = s.recv(4096).decode()
        t1 = time()
        # calculate the time delta (and output if debugging)
        delta = round(t1 - t0, 3)
        if(delta >= 0.2):
                covert_bin += "1"
        else:
                covert_bin += "0"
        if (DEBUG):
                stdout.write(" {}\n".format(delta))
                stdout.flush()

# converting covert_bin into ascii
covert = ""
i = 0
while(i < len(covert_bin)):
    b = covert_bin[i:i+8]
    n = int("0b{}".format(b), 2)
    try:
        if covert[-3:] == "EOF":
            covert = covert[:-3]
            break
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i += 8
s.close()
print(covert)
