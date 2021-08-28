
from typing import List


class solution():
    def minjumps(self,nums:List[int])->int:
        num_elements=len(nums)
        highest_reached_index=0
        reached_distance=0
        num_jumps=0
        if num_elements==1:
            return num_jumps
        for i in range(num_elements-1):
            if i>reached_distance:
                break
            reached_distance=max(reached_distance,nums[i]+i)
            if i==highest_reached_index:
                num_jumps+=1
                highest_reached_index=reached_distance
        return num_jumps

if __name__=='__main__':
    print(solution().minjumps([2,3,1,1,4]))