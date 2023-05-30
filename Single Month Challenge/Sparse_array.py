import re
import os
import sys
def sparse_arrays(strings,query):
    results=[0 for i in range(len(query))]
    count=0
    for q in query:
        for s in strings:
            if s==q:
                results[count]+=1
        count=count+1
    return results

if __name__=="__main__":
    n=int(input())
    strings=[]
    for i in range(n):
        str=input()
        strings.append(str)

    q=int(input())
    query=[]
    for i in range(q):
        str=input()
        query.append(str)

    res=sparse_arrays(strings,query)
    for val in res:
        print(val)