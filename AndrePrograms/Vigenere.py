###################################################################
# Vigenere.py
# Program for encrypting or decrypting text using a vigenere cypher
# Python Version 3.7
# Created by: Andre Aguillard
# Date Modified: 3/29/2020
#
# Program can be run using the following commands:
# python Vigenere.py -e keyName < "file" #Encrpytion*
# python Vigenere.py -d keyName < "file" #Decryption*
# If not using a file, use ctrl+d in linux or ctrl+z in Windows
# for signalling EOF
#
# *Note file must be in the same directory as vigenere.py
#################################################################

from sys import argv, stdin
from string import ascii_lowercase, ascii_uppercase

dict_AlphaUp = {k:v for (v,k) in enumerate(ascii_uppercase, 0)} #letters=keys
dict_NumUp = {k:v for (k,v) in enumerate(ascii_uppercase, 0)} #numbers=keys

dict_AlphaLow = {k:v for (v,k) in enumerate(ascii_lowercase, 0)} #letters=keys
dict_NumLow = {k:v for (k,v) in enumerate(ascii_lowercase, 0)} #numbers=keys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, key):
    ciphertext = ""
    keycounter = 0
    for letter in plaintext: # iterate through each char in string
        if letter not in ALPHABET: # if not a letter or number just insert it
            ciphertext += letter
        else:
            if (letter.isupper()) == True: # do if uppercase
                # compute the letter for the ciphertext
                # find the numeric value of the key + the letter using the dictionary
                # mod by 26 to get the value for the encoded letter
                input = (dict_AlphaLow[key[keycounter]] + dict_AlphaUp[letter]) % 26 # this is a number
                # look up the encoded input and add to the ciphertext
                ciphertext += dict_NumUp[input]
                keycounter += 1
            elif(letter.islower()): # do if lower case
                # compute the letter for the ciphertext
                # find the numeric value of the key + the letter using the dictionary
                # mod by 26 to get the value for the encoded letter
                input = (dict_AlphaLow[key[keycounter]] + dict_AlphaLow[letter]) % 26 # this is a number
                # look up the encoded input and add to the ciphertext
                ciphertext += dict_NumLow[input]
                keycounter += 1
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    keycounter = 0
    for letter in ciphertext: # iterate through each char in string
        if letter not in ALPHABET: # if not a letter or number just insert it
            plaintext += letter
        else:
            if (letter.isupper()) == True: # do if uppercase
                # compute the letter for the ciphertext
                # find the numeric value of the letter - the key using the dictionary
                # mod by 26 to get the value for the encoded letter
                input = (dict_AlphaUp[letter] - dict_AlphaLow[key[keycounter]]) % 26 # this is a number
                # look up the encoded input and add to the ciphertext
                plaintext += dict_NumUp[input]
                keycounter += 1
            else: # do if lower case
                # compute the letter for the ciphertext
                # find the numeric value of the key + the letter using the dictionary
                # mod by 26 to get the value for the encoded letter
                input = (dict_AlphaLow[letter] - dict_AlphaLow[key[keycounter]]) % 26 # this is a number
                # look up the encoded input and add to the ciphertext
                plaintext += dict_NumLow[input]
                keycounter += 1
    return plaintext

mode = argv[1] # first command line parameter is the mode
key = argv[2] # second cmd line parameter
text = stdin.read().rstrip("\n") # get the text from stdin

textLength = len(text.replace(" ","")) # length of text - whitespace
keke = key.replace(" ","") # remove whitespace from key

# To create the master key, repeat the key to at least the desired length
# Then do an array slice to get the exact length
masterKey = (keke * (int(textLength/len(keke))+1))[:textLength]
# Lastly to avoid complications, make the key all lowercase.
masterKey = masterKey.lower()

if (mode == "-e"): # If -e call encrypt function
    ciphertext = encrypt(text, masterKey)
    print(ciphertext)

elif (mode == "-d"):# If -d call decrypt function
    plaintext = decrypt(text, masterKey)
    print(plaintext)
