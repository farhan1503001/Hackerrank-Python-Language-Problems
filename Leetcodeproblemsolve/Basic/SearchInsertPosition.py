from typing import List

class solution():
    def searchInsert(self,nums:List[int],target:int)->int:
        start=0
        end=len(nums)-1
        mid=0
        while start<=end:
            mid=(start+end)//2
            print(start,mid,end)
            if nums[mid]==target:
                break
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        
        return start
    
if __name__=='__main__':
    print(solution().searchInsert([1,3,5,6],7))
    print(solution().searchInsert([1,3,5,6],2))
