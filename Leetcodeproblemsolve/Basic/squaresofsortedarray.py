
from typing import List


class solution():
    def sortedSquares(self,nums:List[int])->List[int]:
        size=len(nums)
        result=[0]*size
        start=0
        end=size-1
        last=size-1
        while(start<=end):
            sq_start=nums[start]*nums[start]
            sq_end=nums[end]*nums[end]
            print(sq_start,sq_end)
            if sq_start>=sq_end:
                result[last]=sq_start
                last-=1
                start+=1
            else:
                result[last]=sq_end
                last-=1
                end-=1
        print(result)
        return result

if __name__=='__main__':
    solution().sortedSquares([-4,-1,0,3,10])
    solution().sortedSquares([-7,-3,2,3,11])
    