# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr
#All Wehrmacht models
LIST_OF_ROTORS = ['I','II','III','IV', 'V']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

#X is not in use, to make your life easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

rotor_s = ['I II III', 'I III II', 'II I III', 'II III I', 'III II I', 'III I II', 'IV II III', 'IV III II', 'II IV III', 'II III IV', 'III II IV', 'III IV II', 'V II III', 'V III II', 'II V III', 'II III V', 'III II V', 'III V II']
ring_setting_s = ['D J B','D B J','J D B','J B D','B D J','B J D']

#there are more reflectors, but this will be bad enough for you to deal with.
LIST_OF_REFLECTORS = ['B', 'C']

message = stdin.read().rstrip("\n")
#This is one way to create an enigma machine, there are others ;)

i=0
while i < len(rotor_s):
	j =0
	while j < len(ring_setting_s):
		Rotors = rotor_s[i]
		RF = 'B'
		RS = ring_setting_s[j]
		PB = 'LO KI JU HY GT FR DE SW QA MP'
		machine = EnigmaMachine.from_key_sheet(rotors=Rotors, reflector='{}'.format(RF),ring_settings='{}'.format(RS),plugboard_settings='{}'.format(PB))
		decrypted_message = machine.process_text(message)
		print(decrypted_message).replace("X", " ")
		j +=1
	i +=1

#machine = EnigmaMachine.from_key_sheet(rotors=rotor_s[5], reflector='C',ring_settings='W H A',plugboard_settings='ZM AS QW DF ER CV BN GH TY JK')
#decrypted_message = machine.process_text(message)
#print(decrypted_message).replace("X", " ")


