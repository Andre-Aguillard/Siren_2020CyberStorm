# Hannah Folkertsma
# CSC 442 - 002
# Program 2 - Vigenere Cipher
# (in python 3.8)
#---------------------------------------------------------------------------------------
from sys import stdin, argv
#getting flag and key from cmd
        #case of key doesnt matter, change it to all lower
alphabetLower = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mode = argv[1]
key = argv[2]

# to get the integer value of any given character
def getValue(ch):
    chValue = 0
    if(ch in alphabetLower):
            for i in range(25):
                if(ch == alphabetLower[i]):
                    chValue = i
    elif(ch in alphabetUpper):
            for i in range(25):
                if(ch == alphabetUpper[i]):
                    chValue = i
    return chValue

# to encrypt the given plaintext to ciphertext using the key
def encrypt(inputText, key):
    cipher = ""
    chValue = 0
    for i in range(len(inputText)):
        ch = inputText[i]
        k = key[i % len(key)]
        while(k == " "):
            i+=1
            #k = key[i%len(key) + 1]
        chValue = getValue(ch)
        kValue = getValue(k)
        newValue = (chValue + kValue) % 26
        if(ch in alphabetLower): # if it is a lowercase letter
            cipher += alphabetLower[newValue]  
        elif(ch in alphabetUpper): # if it is an uppercase letter
            cipher += alphabetUpper[newValue]
        else: # if it is not a letter
            cipher += ch
    
    return cipher

# to decrypt the given ciphertext to plaintext using the key
def decrypt(inputText, key):
    plain = ""
    chValue = 0
    i = 0
    while i < len(inputText):
        k = key[i % len(key)]
        ch = inputText[i]
        if(k == " "):
            i+=1
         #   k = key[i%len(key) + 1]
        chValue = getValue(ch)
        kValue = getValue(k)
        newValue = chValue - kValue % 26
        
        if(ch in alphabetLower): # if it is a lowercase letter
            plain += alphabetLower[newValue]
        elif(ch in alphabetUpper): # if it is an uppercase letter
            plain += alphabetUpper[newValue]
        else: # if it is not a letter
            plain += ch
        i+=1
    return plain

inputText = ""

#reading from stdin
text = stdin.read().split("\n")
for line in text:
    inputText = line.rstrip("\n")
        
    if(mode == "-e"): #encrypting
        cipher = encrypt(inputText, key)
        print(cipher)
    elif(mode == "-d"): #decrypting
        plain = decrypt(inputText, key)
        print(plain)

