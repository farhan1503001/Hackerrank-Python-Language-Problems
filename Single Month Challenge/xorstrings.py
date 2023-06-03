import re
import os
import math

def xorstring(s,t):
    res=""
    for i in range(len(s)):
        if s[i]==t[i]:
            res=res+"0"
        else:
            res=res+"1"
    return res

if __name__=="__main__":
    s=input()
    t=input()
    print(xorstring(s,t))