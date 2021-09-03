
from typing import List


class solution():
    def maxSubArray(self,nums:List[int])->int:
        if len(nums)==0:
            return 0
        current_sum=nums[0] #first value is maximum sum currently
        max_sum=current_sum
        for i in range(1,len(nums)):
            #update current sum
            temp=current_sum+nums[i]
            print(i,nums[i],temp)
            if temp>nums[i]:
                current_sum=temp
            else:
                current_sum=nums[i]
            #update max value
            max_sum=max(max_sum,current_sum)
        print(max_sum)
        return max_sum

if __name__=='__main__':
    solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    solution().maxSubArray([5,4,-1,7,8])
        