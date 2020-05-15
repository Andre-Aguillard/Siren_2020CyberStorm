# readBin.py
#
# read a binary file and print it out as hex

from binascii import hexlify

with open('hashes',"rb") as f:
    contents = hexlify(f.read())
    print(contents)
    print("")
