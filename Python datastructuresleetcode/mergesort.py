from typing import List
class solution():
    def sort(self,arr:List[int],start:int,end:int)->None:
        if end<=start:
            return
        mid=(start+end)//2
        self.sort(arr,start,mid)
        self.sort(arr,mid+1,end)
        self.merge(arr,start,mid,end)
    def merge(self,arr:List[int],start:int,mid:int,end:int)->None:
        #creating temporary array for merging with size end-start+1
        temp_arr=[]
        left=start
        right=mid+1
        while(left<=mid and right<=end):
            if arr[left]<=arr[right]:
                temp_arr.append(arr[left])
                left+=1
            elif arr[left]>arr[right]:
                temp_arr.append(arr[right])
                right+=1
        if left<=mid:
            while(left<=mid):
                temp_arr.append(arr[left])
                left+=1
        elif right<=end:
            while(right<=end):
                temp_arr.append(arr[right])
                right+=1
        for i in range(len(temp_arr)):
            arr[start+i]=temp_arr[i]

if __name__=='__main__':
    arr=[2,6,1,5,2,12,9]
    solution().sort(arr,0,len(arr)-1)
    print(arr)

