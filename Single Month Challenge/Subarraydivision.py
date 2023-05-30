import os
import re
import sys

def birthday(s,d,m):
    n=len(s)
    count=0
    if n==1:
        if s[0]==d:
            return 1
        else:
            return 0
    for i in range(0,n-m+1):
        sum=0
        for j in range(i,i+m):
            #print(s[j],end="  ")
            sum=sum+s[j]
        if sum==d:
            count=count+1
        print()
    #print(count)
    return count


if __name__=="__main__":
    n=int(input())
    s=list(map(int,input().rstrip().split()))
    d,m=map(int,input().rstrip().split())
    res=birthday(s,d,m)
    print(res)