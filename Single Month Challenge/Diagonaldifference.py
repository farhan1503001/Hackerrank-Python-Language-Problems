import math
import sys
import re
def diagonal_difference(arr,n):
    lsum=0
    rsum=0
    for i in range(n):
        lsum+=arr[i][i]
        rsum+=arr[i][n-i-1]
    diff=abs(lsum-rsum)
    #print(diff)
    return diff

if __name__=="__main__":
    n=int(input())
    arr=[]
    for i in range(n):
    
        temp=list(map(int,input().rstrip().split()))
        #print(temp)
        arr.append(temp)

    print(diagonal_difference(arr,n))
    
