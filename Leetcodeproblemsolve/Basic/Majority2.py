
from typing import List


class solution():
    def majorityElement(self,nums:List[int])->List[int]:
        if(len(nums)==1):
            return nums[0]
        memory=dict()
        condition=len(nums)//3
        elements=list()
        for i in range(len(nums)):
            if nums[i] not in memory:
                memory[nums[i]]=1
            else:
                memory[nums[i]]+=1
                if memory[nums[i]]>condition:
                    elements.append(nums[i])
        print(elements)
        return elements

if __name__=='__main__':
    solution().majorityElement([3,2,3])
