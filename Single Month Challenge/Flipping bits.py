import math
import re
import sys

def flipping_bits(number):
    #First convert to binary 
    bits_array=[0 for i in range(32)]
    pref=0
    while number!=0:
        temp=number%2
        bits_array[-1-pref]=temp
        pref=pref+1
        number=number//2
    #print(bits_array)
    multiplier=1
    count=-1
    newnumber=0
    
    while count!=-33:
        if bits_array[count]==0:
            bits_array[count]=1
        else:
            bits_array[count]=0
        
        
        newnumber+=bits_array[count]*multiplier
        count=count-1
        multiplier*=2
    #print(newnumber)
    return newnumber
    
    #print(bits_array)
if __name__=="__main__":
    q=int(input())
    for i in range(q):
        n=int(input())
        res=flipping_bits(n)
        print(res)

