from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums:List[int], k: int) -> bool:
        memory=dict()
        for index,val in enumerate(nums):
            if val not in memory:
                memory[val]=index
            else:
                if abs(memory[val]-index)<=k:
                    return True
                else:
                    memory[val]=index
        return False

if __name__=='__main__':
    print(Solution().containsNearbyDuplicate([1,2,3,1],3))         
