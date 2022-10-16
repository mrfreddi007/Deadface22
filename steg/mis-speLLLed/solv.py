#!/usr/bin/env python3
import re
import string

alph = string.ascii_letters

def rot23(encflag):
    flag = ""
    for i in encflag:
        ind = alph.index(i)
        flag += alph[(ind+23)%26]
    return flag

original1 = ""
enc1 = ""

with open("pumpkin-scary-faces-steg.txt","rb") as f:
    enc = f.read().split(b"\r\r")
    
with open("original.txt","rb") as f:
    original = f.read().split(b"\n\n")
    
    
for i, line in enumerate(enc):
    encwords = line.split(b" ")
    origwords = original[i].split(b" ")
    for j, encword in enumerate(encwords):
        
        encword1 = ""
        for k, char in enumerate(encword):
            if chr(char).isprintable() and chr(char) in alph:
                encword1 += chr(char)
        
        origword = ""
        for k, char in enumerate(origwords[j]):
            if chr(char).isprintable() and chr(char) in alph:
                origword += chr(char)
                
        for k, char in enumerate(encword1):
            if char != origword[k]:
                enc1 += char
                original1 += origword[k]
    
flag = rot23(original1)
print("flag{"+flag+"}")