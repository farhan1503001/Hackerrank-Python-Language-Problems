import math
import sys
import re
import os

def pangrams(string:str):
    str=string.lower().replace(" ","")
    #print(str)
    arr=[False for i in range(26)]
    #print(arr)
    for char in str:
        index=int(ord(char))-97
        #print(index)
        arr[index]=True

    for i in range(26):
        if arr[i]==False:
            return "not pangram"
    return "pangram"

if __name__=="__main__":
    s=input()
    print(pangrams(s))