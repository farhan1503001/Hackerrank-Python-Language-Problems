
from typing import List


class solution():
    def missingNumber(self,nums:List[int])->int:
        cal_sum=sum(nums)
        actual_sum=(len(nums)*(len(nums)+1))/2
        return int(actual_sum-cal_sum)#missing value

if __name__=='__main__':
    print(solution().missingNumber([3,0,1]))