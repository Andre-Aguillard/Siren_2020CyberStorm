#Hannah Folkertsma
# program 1 - binary decoder
# March 24, 2020
# (in python 3.8)
#----------------------------------------------------------------------------------
import sys

# get binary from stdin
file = sys.stdin
binary_input = file.read()

# determine if it is 7 or 8 bit ascii
input_length = int(len(binary_input)) -1
if(input_length % 7 == 0):
    bits = 7
else:
    bits = 8
# separate the bits into a list
binary_split = []
ascii_output = []
for i in range(int(input_length/bits)):
    binary_split.append(binary_input[i*bits:(i+1)*bits])

# converting to ascii characters
counter = 0
for chunk in binary_split:
    decimal = int(chunk, 2)
    character = chr(decimal)
    #if(character == "\x08"):
    #  if(counter > 0):
     #       del ascii_output[counter-1]
   # else:
    ascii_output.append(character)
    counter+=1
print(''.join(ascii_output))
