from typing import List
class solution():
    def mountain_array_find(self,arr:List[int])->bool:
        length=len(arr)
        count=0
        while(count<length and arr[count]<arr[count+1]):
            count+=1
        #First check 
        if count==0 or count==length:
            return False
        #print(count)
        #second check decreament
        while(count<length-1 and arr[count]>arr[count+1]):
            count+=1
        #print(count)
        return count==length-1

if __name__=='__main__':
    arr=[0,2,3,4,5,2,1,0]
    print(solution().mountain_array_find(arr))