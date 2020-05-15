import sys
from sys import argv
#reciever file
crypt = sys.stdin.read()
key = argv[1]

#open key file in same directory and read
f = open(key,'r')
message = f.read()
messageAr = bytearray(message)
cryptAr = bytearray(crypt)
index = 0
string = ""

#encrypt / decrpyt loop
for x in cryptAr:
	n = x^messageAr[index]
	index += 1
	string += chr(n)
print string
