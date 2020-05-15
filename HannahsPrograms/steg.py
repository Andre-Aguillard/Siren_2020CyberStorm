# Hannah Folkertsma
# CSC 442 - 002
# May 8, 2020
# Program 7: Steg (python 3.8)
#--------------------------------------------------------------------------------
import sys
import binascii
SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])
offset = 0
interval = 1

# get input from argv
for arg in sys.argv:
    if(arg == "-s"):
        action = "store"
    elif(arg == "-r"):
        action = "retrieve"
    elif(arg == "-b"):
        mode = "bit"
    elif(arg == "-B"):
        mode = "byte"
    elif(arg[:2] == "-o"):
        offset = int(arg[2:])
    elif(arg[:2] == "-i"):
        interval = int(arg[2:])
    elif(arg[:2] == "-w"):
        wrapper_file = open(arg[2:],"rb")
        wrapper_bytes = bytearray(wrapper_file.read())
    elif(arg[:2] == "-h"):
        hidden_file = open(arg[2:], "rb")
        hidden_bytes = bytearray(hidden_file.read())
    
# method to store a hidden file in a wrapper using the byte method
def byteStore(SENTINEL, offset, interval, wrapper_bytes, hidden_bytes):
        i = 0
        while(i < len(hidden_bytes) and (offset < len(wrapper_bytes))):
            wrapper_bytes[offset] = hidden_bytes[i]
            offset += interval
            i+=1
        i = 0
        while(i < len(SENTINEL) and (offset < len(wrapper_bytes))):
            wrapper_bytes[offset] = SENTINEL[i]
            offset += interval
            i += 1
        return wrapper_bytes
    
# method to retrieve a hidden file from a wrapper 
def byteRetrieve(SENTINEL, offset, interval):
        hidden = bytearray()
        isDone = False
        while(offset < len(wrapper_bytes)):
            b = wrapper_bytes[offset]
            # if B is the first sentinel byte, check for the rest of the sentinel
            if(b == SENTINEL[0]):
                offsettmp = offset
                isNotSentinel = False
                for i in SENTINEL:
                    offsettmp += interval
                    if i != wrapper_bytes[offsettmp]:
                        isNotSentinel = True
                        isDone = True
                    if(not isNotSentinel):
                        return hidden
            else:
                if(not isDone):
                    hidden.append(b)
            offset+=interval
        return hidden

# method to store a hidden file inside a wrapper using the bit method
def bitStore(SENTINEL, offset, interval, wrapper_bytes, hidden_bytes):
            # storing the hidden file
            i = 0
            while(i < len(hidden_bytes) and offset<len(wrapper_bytes)):
                for j in range(8):
                    wrapper_bytes[offset] &= 0b11111110
                    wrapper_bytes[offset] |= ((hidden_bytes[i] & 0b10000000) >> 7)
                    hidden_bytes[i] = (hidden_bytes[i] << 1) & (0b11111111)
                    offset+=interval
                i+=1

            # storing the sentinel
            i = 0
            while(i < len(SENTINEL) and offset<len(wrapper_bytes)):
                for j in range(8):
                    wrapper_bytes[offset] &= 0b11111110
                    wrapper_bytes[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                    SENTINEL[i] = (SENTINEL[i] << 1) & (0b11111111)
                    offset +=  interval
                i+=1
            return wrapper_bytes
        
# method to retrieve a hidden file from a wrapper using the bit method
def bitRetrieve(SENTINEL, offset, interval):
        w = wrapper_bytes
        hidden = bytearray()
        maybeSentinel = bytearray()
        lastWasSentinel = True
        while(offset < (len(w) - 8*interval)):
            b = 0
            for j in range(8):
                b |= (w[offset] & 0b00000001)
                if(j < 7):
                    b = (b << 1) & 0b11111111
                    offset += interval
            # if b is in the sentinel and the last byte was also in the sentinel,
            # add b to the sentinel array
            if(b in SENTINEL and lastWasSentinel):
                maybeSentinel.append(b)
                lastWasSentinel = True
            # if b is not part of the sentinel, clear the sentinel array
            else:
                lastWasSentinel = False
                maybeSentinel = bytearray()
            if(maybeSentinel == SENTINEL):
                return hidden;
            hidden.append(b)
            offset += interval
            
        return hidden
    

    
# byte method storage
if(mode == "byte" and action == "store"):
    stored = byteStore(SENTINEL, offset, interval, wrapper_bytes, hidden_bytes)
    sys.stdout.buffer.write(stored)

#byte method extraction
elif(mode == "byte" and action == "retrieve"):
    hidden = byteRetrieve(SENTINEL, offset, interval)
    sys.stdout.buffer.write(hidden)
    
#bit method storage
elif(mode == "bit" and action == "store"):
    stored = bitStore(SENTINEL, offset, interval, wrapper_bytes, hidden_bytes)
    sys.stdout.buffer.write(stored)

#bit method extraction
elif(mode == "bit" and action == "retrieve"):
    hidden = bitRetrieve(SENTINEL, offset, interval)
    sys.stdout.buffer.write(hidden)
