# Hannah Folkertsma
# CSC 442 - 002
# Program 3 - FTP Storage Covert Channel
# March 31, 2020
# (in python 3.8)
# ----------------------------------------------------------------------------------
from ftplib import FTP

# constants
IP = "jeangourd.com"
PORT = 21
DIRECTORY = "7"
METHOD = 7

# the folder contents
ftp_contents = []

# method to decode the binary to ascii
def decode(binary, bits):
    binary_split = []
    ascii_output = []
    for i in range(int(len(binary)/bits)):
        binary_split.append(binary[i*bits:(i+1)*bits])

    # converting to ascii characters
    counter = 0
    for chunk in binary_split:
        decimal = int(chunk, 2)
        character = chr(decimal)
        if(character == "\x08"):
            if(counter > 0):
                try:
                    del ascii_output[counter-1]
                except IndexError:
                    pass
        else:
            ascii_output.append(character)
        counter+=1
    print(''.join(ascii_output))


# connect to FTP
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(DIRECTORY)
# get files
ftp.dir(ftp_contents.append)
# disconnect
ftp.quit()

#the permissions
perms = ""
#the permissions converted to binary
binary_perms = ""

for row in ftp_contents:
    row2 = row.split(" ")

    if(METHOD == 7):
        # removing the first 3 bits
        if(row2[0][0:3] == "---"):
            perms += row2[0][3:]
    elif(METHOD == 10):
        perms += row2[0]
    
for ch in perms:
    if(ch == "-"):
        binary_perms += "0"
    else:
        binary_perms += "1"

print("7-bit:")
decode(binary_perms, 7)
print("8-bit:")
decode(binary_perms, 8)
        





    
