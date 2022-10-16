#!/usr/bin/env python3
from bitstring import BitArray

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def checkParity(bin):
    partall = str((bin[:-1].count("1") + 1)%2 )
    if bin[-1] == partall:
        return True
    else:
        return False

with open("./uniwack-formatted-message.txt","rb") as f:
    fil = BitArray(bytes=f.read()).bin

korrekt = ""
for i in range(0,len(fil),19):
    if i > len(fil) - 7:
        break
    a = fil[i:i+19]
    if checkParity(a):
        f = a[0:8] 
        l = a[9:-2]
        print(f)
        korrekt += f[::-1] + l[::-1]
        
with open("traffik.txt","w") as f:
    f.write(bitstring_to_bytes(korrekt).decode())
print(bitstring_to_bytes(korrekt).decode())