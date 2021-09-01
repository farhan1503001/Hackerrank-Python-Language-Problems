
from typing import List
class solution():
    def findDisappearedNumbers(self,nums:List[int])->List[int]:
        '''
        Find the value the negate/flag then index value ==value 
        '''
        for value in nums:
            if nums[abs(value)-1]>0:
                #as 0 indexed
                nums[abs(value)-1]=nums[abs(value)-1]*-1
        result=[]
        for index,value in enumerate(nums):
            if value>0:
                result.append(index+1)
        return result

if __name__=='__main__':
    print(solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))