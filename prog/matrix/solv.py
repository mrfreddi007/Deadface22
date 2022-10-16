#!/usr/bin/env python3
from pwn import *

r = remote("code.deadface.io",50000)
a = r.recv().decode()[1:-2].split("]\n[")
print(a)
sum = 0
for i in a:
    smallest = 99999999999
    for j in i.split(", "):
        if int(j) < smallest:
            smallest = int(j)
    sum += smallest
    print(smallest)
    
r.sendline(str(sum))
print(r.recv())
