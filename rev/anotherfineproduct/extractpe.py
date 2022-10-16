#!/usr/bin/env python3

with open("re03-another-fine-product.exe","rb") as f:
    file = f.read()
    
newexe = b""
x = 170
for i, byte in enumerate(file):
    if i >= 0x1000:
        newexe += (byte ^ x).to_bytes(1,'big')
        x = byte
        
with open("new.exe","wb") as f:
    f.write(newexe)