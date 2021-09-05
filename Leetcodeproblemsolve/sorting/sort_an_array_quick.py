from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums
    def quicksort(self,nums:List[int],start:int,end:int)->None:
        if start<end:
            position=self.partision(nums,start,end)
            self.quicksort(nums,start,position-1)
            self.quicksort(nums,position+1,end)
    def partision(self,nums:List[int],start:int,end:int)->int:
        sorting_index=start-1
        current_index=start
        pivot_value=nums[end]
        while current_index<=end:
            if nums[current_index]<=pivot_value:
                sorting_index+=1
                nums[sorting_index],nums[current_index]=nums[current_index],nums[sorting_index]
            current_index+=1
        return sorting_index

if __name__=='__main__':
    print(Solution().sortArray([5,2,3,1]))