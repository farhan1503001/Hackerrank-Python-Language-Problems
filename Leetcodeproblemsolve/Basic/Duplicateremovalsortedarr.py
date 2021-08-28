
from typing import List


class solution():
    def removeDuplicates(self,nums:List[int])->int:
        i=0#starting index
        j=i+1
        while(j<len(nums)):
            if nums[i]==nums[j]:
                j+=1
            else:
                i=i+1
                nums[i]=nums[j]
                j=j+1
        print(nums[:i+1])
        return i+1 #size=index+1

if __name__=='__main__':
    arr=[0,0,1,1,1,2,2,3,3,4]
    print(solution().removeDuplicates(arr))
