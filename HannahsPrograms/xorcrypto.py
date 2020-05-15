# Hannah Folkertsma
# CSC 442 - 002
# May 8, 2020
# Program 6 - XOR Crypto (python 2)
#---------------------------------------------------------------------------------
from sys import stdin, stdout

# take in key from the specified file
key_file = open("key1", "rb")
key = key_file.read()

key_file.close()
# take in text from stdin
input_text = stdin.read()

# XOR the input with the key
result = ""
k = 0
for i in range(len(input_text)):
    result += chr(ord(input_text[i])^ord(key[k]))
    k = (k + 1)%len(key)
    i+=1
print(result)
