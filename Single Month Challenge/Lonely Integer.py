import math
import os
import re
import sys

def lonely_integer(array):
    """
    Basic dictionary problem
    """
    dictionary=[0 for i in range(101)]
    for val in array:
        dictionary[val]+=1

    for i in range(1,101):
        if dictionary[i]==1:
            return i

    

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().rstrip().split()))
    print(lonely_integer(arr))