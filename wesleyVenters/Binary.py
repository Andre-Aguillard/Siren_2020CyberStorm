from sys import stdin
#written in the default python for Kali Linux

def decode(binary,n):
        text = ""
        i = 0
        
        while (i < len(binary)):
                
                byte = binary[i:i+n]
                byte = int(byte, 2)
                if(byte==8):#checks if the integer is th ascii value for backspace
                    text = text[:-1]#removes the last character of the string text
                if(byte!=8):#if it isnt backspace then it continues as normal
                    text += chr(byte)
                i += n
                
                
        return text

binary = stdin.read().rstrip("\n")

#if(len(binary) % 7 == 0):
text = decode(binary,7)

print text
text = decode(binary,8)

print text

#if(len(binary)% 8 == 0):
#infection:In linux, the code given didnt do anything except continuously return
#the sentence, Can not Fork, in windows it slowed down the vm alot and i ended up
#stoping it, i believe this is another way of using a "fork bomb" and attackers
# can use it to slow down or maybe even crash computers, giving them more
#time to do what they need to do to get your information
# as for how to stop it you could possibly place a limiter on how much space 
# a computer gives any certain thing to run, as to not take up the entire system
