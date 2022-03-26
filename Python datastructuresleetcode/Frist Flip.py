#This program reverses the elements of an array in odd position
from typing import List
def flip_half(arr:List[int])->List[int]:
    start=1
    if (len(arr))%2==0:
        end=len(arr)-1
    else:
        end=len(arr)
    print("END is: ",end)
    while(start<end):
        temp=arr[end]
        arr[end]=arr[start]
        arr[start]=temp
        #bijor theke 2 samne ba pichone gele bijor paoa jai
        start+=2
        end-=2
        
    print(arr)
    return arr
if __name__=='__main__':
    res=flip_half([1,8,7,2,9,18,12,None])
    print(res)
    