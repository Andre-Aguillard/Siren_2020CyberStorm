#Jake Latino
# 8)    < me with cool sunglasses
from sys import stdin, argv

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def remove(string):
    return string.replace(" ", "") #this removes the spaces from the key if there are any when it's recieved as input
                                    #for some reason if i try to remove the spaces after the key goes into encrypt or decryp
                                    # it just doesn't work and the key stays the same

def encrypt(plaintext, key):

    brokeArray = []
    keyIndex = 0
    key = key.upper()


    

    for i in plaintext:
        num = ALPHABET.find(i.upper())
        if(num != -1):


            num += ALPHABET.find(key[keyIndex])#
            num %= len(ALPHABET)


            if i.isupper():
                brokeArray.append(ALPHABET[num])#check to see if it's  uppercase
            elif i.islower():
                brokeArray.append(ALPHABET[num].lower())# check to see if it's lowercase

            keyIndex += 1 #move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0

        else:
            brokeArray.append(i)#if the symbol is not found in ALPHABET just put it in as it is

        
    return "".join(brokeArray) #doing this instead of what was shown in the video because it's easier for the array

def decrypt(ciphertext, key):

    fixArray = []
    keyIndex = 0
    key = key.upper()
    
    key.replace(" ", "")

    for i in ciphertext:
        num = ALPHABET.find(i.upper())
        if(num != -1):
            num -= ALPHABET.find(key[keyIndex]) #subtract here
            num %= len(ALPHABET)

            if i.isupper():
                fixArray.append(ALPHABET[num])
            elif i.islower():
                fixArray.append(ALPHABET[num].lower())

            keyIndex += 1 #move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0

        else:
            fixArray.append(i)

        
    return "".join(fixArray)




mode = argv[1]
key = argv[2]


text = stdin.read().rstrip("\n")


if(mode == "-e"):
    ciphertext = encrypt(text, remove(key))
    print ciphertext
elif(mode == "-d"):
    plaintext = decrypt(text, remove(key))
    print plaintext

