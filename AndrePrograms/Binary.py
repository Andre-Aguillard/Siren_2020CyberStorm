#####################################################
# Binary.py
# Program for decoding 8 or 7 bit ASCII to Binary
# Python Version 3.7
# Created by: Andre Aguillard
# Date Modified: 3/24/2020
#
# Program can be run using the following commands:
# python Binary.py < "filename.txt"
# OR python Binary.py "filename"
# Note file must be in the same directory as Binary.py
#####################################################

import sys
# Binary Decoder funciton
# INPUT: binary data
# OUTPUT: decoded ASCII message
def binaryDecoder(data):
    message = ""
    print(len(data))
    if (len(data) % 7 == 0):
        n = 7
    elif (len(data) % 8 == 0):
        n = 8
    else:
        message = "Binary data is neither 7 or 8 bits. You fool."
        print(len(data))
        return message
    i = 0
    message_ctr = 0
    while (i < len(data)):
        byte = data[i:i+n]
        #print (byte)
        ascii = int(byte,2)
        if ascii == 8: # backspace character
            if message_ctr > 0: #in case first character is a backspace
                                # if it is, just skip it.
                # DEBUG : the below statment is used for debugging
                ### print ("backspace {}".format(message_ctr))

                # replaces the character at the last index (msg_ctr-1) with nothing
                message = message.replace(message[message_ctr-1],"")
                message_ctr -= 2
                #go back two indicies for both the bck and the deleted chr
        else:
            message += chr(ascii)
            # DEBUG : the below statment is used for debugging
            ### print("{}:{}={} = {}".format(message_ctr,byte,ascii,chr(ascii) ))
            #increments the counter everytime something is added to the message
            message_ctr += 1
        i += n
    return message

# Main program
# input is either in the command line or from stdin
if __name__ == "__main__":
    bin = ''
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            for line in f:
                bin += line.rstrip("\n")
    else:
        for line in sys.stdin:
            bin += line.rstrip("\n")

    print(binaryDecoder(bin))
