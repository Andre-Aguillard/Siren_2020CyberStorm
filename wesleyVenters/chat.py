#Wesley Venters
#program 4
#for my program i have made it to where you only have to actually edit the program variable is if
#the zero timing needs to be bigger than the one by making the timing arguments 3 and for
#so when you run the code it should be (python2.7 i believe):
#python chat.py "ip" "port" "zero timing" "one timing"
import socket
from sys import stdout, argv
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# decode binary

def decode(binary, n):
        text = ""
        i = 0
        while (i < len(binary)):
                byte = binary[i:i+n]
                byte = int(byte, 2)
                if(byte==8):#checks if the integer is th ascii value for backspace
                    text = text[:-1]#removes the last character of the string text
                if(byte!=8):#if it isnt backspace then it continues as normal
                    text += chr(byte)
                i += n

        return text

# set the server's IP address and port
ip = argv[1]
port = argv[2]
port = int(port)
#Zero and One timing
ZERO = argv[3]
ZERO = float(ZERO)
ONE = argv[4]
ONE = float(ONE)
# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
covertbin = ""
counter=0
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta (and output if debugging)
        delta = round(t1 - t0, 3)
        if (delta >= ONE):
            covertbin += "1"
        elif (delta <= ZERO):
            counter+=1
        else:
            covertbin += "0"
	if (DEBUG):
            stdout.write(" {}\n".format(delta))
            stdout.flush()
#decode and print message
covert = ""
#uncomment for 7 bit
#covert = decode(covertbin, 7)
#uncomment for 8 bit
covert = decode(covertbin,8)
print covert
covert = decode(covertbin,7)
print covert

print covertbin
# close the connection to the server
s.close()

