
from typing import List


class solution():
    def sortArray(self,nums:List[int])->List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums

    def mergeSort(self,nums:List[int],start:int,end:int)->None:
        if start>=end:
            return
        mid=(start+end)//2
        self.mergeSort(nums,start,mid)
        self.mergeSort(nums,mid+1,end)
        self.merge(nums,start,mid,end)
    def merge(self,nums:List[int],start:int,mid:int,end:int)->None:
        temp=list()
        left=start
        right=mid+1

        while(left<=mid and right<=end):
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        
        if left<=mid:
            while left<=mid:
                temp.append(nums[left])
                left+=1
        elif right<=end:
            while right<=end:
                temp.append(nums[right])
                right+=1

        for i in range(len(temp)):
            nums[start+i]=temp.pop(0)

if __name__=='__main__':
    print(solution().sortArray([1,4,2,5,7,2,9]))
