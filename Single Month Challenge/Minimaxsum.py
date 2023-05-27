import math
import os
import random
import re 
import sys


def minimaxsum(array):
    mini_sum=0
    max_sum=0
    for i in range(4):
        mini_sum+=arr[i]
        max_sum+=arr[len(arr)-1-i]
    print(mini_sum,max_sum)

if __name__=="__main__":
    arr=list(map(int, input().rstrip().split()))
    minimaxsum(arr)