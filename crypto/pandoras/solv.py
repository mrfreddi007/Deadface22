#!/usr/bin/env python3
import string

enc = "guvz qgz pfv tvb"
nums = "3686 526 814 518"

alph = string.ascii_lowercase
flag = ""

for i, a in enumerate(enc):
    if a != " ":
        ind = alph.index(a)
        flag += alph[(ind - int(nums[i])) % 26]
    else:
        flag += " "

print(flag)