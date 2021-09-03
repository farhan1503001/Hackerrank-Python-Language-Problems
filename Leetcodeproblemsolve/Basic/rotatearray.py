
from typing import List


class solution():
    def rotate(self,nums:List[int],k:int)->None:
        reversed_arr=[0]*len(nums)
        for i in range(len(nums)):
            reversed_arr[(i+k)%len(nums)]=nums[i]
        
        nums[:]=reversed_arr
        print(nums)

if __name__=='__main__':
    solution().rotate([1,2,3,4,5,6,7],3)