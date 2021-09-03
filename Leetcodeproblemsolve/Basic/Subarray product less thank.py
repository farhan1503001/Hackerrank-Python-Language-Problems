
from typing import List


class solution():
    def numProductLessThanK(self,nums:List[int],k:int)->int:
        if k<=1:
            return 0
        left=0
        counter=0
        product=1
        for i in range(len(nums)):
            product=product*nums[i]
            while(product>=k):
                product=product/nums[left]
                left+=1
            counter+=(i-left+1)
        return counter

if __name__=='__main__':
    print(solution().numProductLessThanK([10,5,2,6],100))
