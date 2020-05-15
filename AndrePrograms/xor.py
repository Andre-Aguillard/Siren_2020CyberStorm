########################################################################
# xor.py
# Program to run an xor encryption or decryption on a file.
#
# Python Version: 3.6.8
# Run Program: python xor.py < ciphertext OR python xor.py < plaintext
#
# Program reads the key from a file namedd key in the current directory
# If you want to use a different key file edit the name in line 16
########################################################################
import sys

# Debug global variable
DEBUG = False

KEYFILE = 'key'

# Read the input file from stdin as binary
def get_input():
    try:
        return bytearray(sys.stdin.buffer.read())
    except:
        return print("Error reading from stdin")

def bxor (b1, b2):
    output = bytearray()
    for b1, b2 in zip(b1, b2):
        output.append(b1 ^ b2)
    return output

# Read the contents of key into a bytearray
with open(KEYFILE,'rb') as f:
    key_contents = bytearray(f.read()) # the whole file is read into the string
    key_length = len(key_contents) # length of the key in bytes
                                   # key1 from gourx is 74 bytes

# find the length of the input
input = get_input()
input_length = len(input)
if (DEBUG):
    print("Key length in bytes is:      {}".format(key_length))
    print("Input length in bytes is:    {}".format(input_length))

if (key_length == input_length):
    if(DEBUG):
        print("Key and input lengths are equal...")
        print("Sending output to standard out.\n")
    output = bxor(input, key_contents)
    sys.stdout.buffer.write(output)

else: #This is the case if the key is not the same size as the message
    if (input_length % key_length == 0):
        # the input is some multiple of the key length so we can attempt to xor
        multiplier = input_length / key_length
        new_key = bytearray()
        while (multiplier > 0):
            new_key.append(key_contents)
            multipler -= 1
        output = bxor(input, new_key)
        sys.stdout.buffer.write(output)

    if (key_length > input_length):
        # need to ony use as much of the key as needed
        new_key = key_contents
        new_key[input_length+1:key_length] = [] # this should delete the uneeded bytes
        output = bxor(input, new_key)
        sys.stdout.buffer.write(output)



# Using key with ciphertext1, the resulting phrase is:
# Hello, my name is Indigo Montoya.  You killed my father.  Prepare to die!

# Using the key2 with ciphertext2, I get the image of last year's poster

# Ran the following three commands and got no errors or differences in files
### aca@aca-CyberStorm:~/Cyber/XOR program$ python3 xor.py < ciphertext1 > plaintext1
### aca@aca-CyberStorm:~/Cyber/XOR program$ python3 xor.py < plaintext1 > newciphertext1
### aca@aca-CyberStorm:~/Cyber/XOR program$ diff newciphertext1 ciphertext1
