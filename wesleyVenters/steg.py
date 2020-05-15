#program7 shift =   B = (B << shift) & (2**8-1)
from sys import stdin,stdout,argv

debug = False
sentinel = bytearray([0x0,0xff,0x0,0x0,0xff,0x0])
mode = argv[1]
method = argv[2]
offset = argv[3]
offset = offset.strip("-o")
offset = int(offset)

interval = argv[4]
interval = interval.strip("-i")
interval = int(interval)

wrapper = argv[5]
wrapper = wrapper.strip("-w")

try:
    hidden = argv[6]
except IndexError:
    hidden = None
if(hidden != None):
    hidden = hidden.strip("-h")
        
if debug == True:
    print "mode:{} method:{} offset:{} interval:{} wrapper:{} hidden{}".format(mode,method,offset,interval,wrapper,hidden)


if(method == "-B"):
    if(mode == "-s"):
        wrapdata = open(wrapper, "r")
        wrapbyte = bytearray(wrapdata.read())
        hiddata = open(hidden, "r")
        hidbyte = bytearray(hiddata.read())
        i = 0
        while (i < len(hidbyte)):
            wrapbyte[offset] = hidbyte[i]
            offset += interval
            i +=1
        j=0
        while (j < len(sentinel)):
            wrapbyte[offset] = sentinel[j]
            offset += interval
            j+=1
        print wrapbyte
    elif(mode == "-r"):
        wrapdata = open(wrapper, "r")
        wrapbyte = bytearray(wrapdata.read())
        hidbyte = bytearray()
        tempset = bytearray()
        count = 0
        while(offset < len(wrapbyte)):
            x = wrapbyte[offset]
            if (x == sentinel[0]):
                while (x == sentinel[count]):
                    count += 1
                    offset += interval
                    tempset.append(x)
                    x = wrapbyte[offset]
                    if count == len(sentinel):
                        print hidbyte
                        exit()
                for i in tempset:
                    hidbyte.append(i)
                tempset = bytearray()
                count = 0
            hidbyte.append(x)
            offset += interval


if (method == "-b"):
      if (mode == "-s"):
         wrapdata = open(wrapper, "r")
         wrapbyte =  bytearray(wrapdata.read())
         hiddata = open(hidden, "r")
         hidbyte = bytearray(hiddata.read())
         i = 0
         while (i < len(hidbyte)):
              for j in range(0,8):
                    wrapbyte[offset] = wrapbyte[offset] &  11111110
                    wrapbyte[offset] |= ((hidbyte[i] & 10000000) >> 7) 
                    hidbyte[i] = (hidbyte[i] << 1) & (2 ** 8 -1)
                    offset += interval
              i += 1
         i = 0
         while(i < len(sentinel)):
            for j in range(0, 8):
                wrapbyte[offset] &= 11111110
                wrapbyte[offset] |= ((sentinel[i] & 10000000) >> 7)
                sentinel[i] = (sentinel[i] << 1) & (2 ** 8 - 1)
                offset += interval
            i += 1
         print wrapbyte
 
      elif (mode == "-r"):
            wrapdata = open(wrapper, "r")
            wrapbyte =  bytearray(wrapdata.read())
            hidbyte = bytearray()
            tempset = bytearray()
            count = 0
            while (offset < len(wrapbyte)):
                x = 0
                for j in range(0,8):
                    x |= (wrapbyte[offset] & 0b00000001)
                    if j < 7:
                        x = (x << 1) & (2 ** 8 - 1)
                        offset += interval
                if (x == sentinel[0]): 
                    while (x  == sentinel[count]):
                        count += 1
                        offset += interval
                        tempset.append(x)
                        x = 0
                        for j in range(0,8):
                            x |= (wrapbyte[offset] & 0b00000001)
                            if j < 7:
                                x = (x << 1) & (2 **8 -1)
                                offset+= interval
                        if count == len(sentinel):
                            print hidbyte
                            exit()
                    for i in tempset:
                        hidbyte.append(i)
                    tempset = bytearray()
                    count = 0
                hidbyte.append(x)
                offset += interval


