from typing import List
class solution():
    answer=list()
    def backtrack(self,first:int,combination:List[int],nums:List[int],k:int)->None:
        if len(combination)>k:
            return
        if len(combination)==k:
            self.answer.append(combination.copy())
        
        for i in range(first,len(nums)):
            combination.append(nums[i])
            self.backtrack(i+1,combination,nums,k)
            combination.pop()
            
        
    def subsets(self,nums:List[int])->List[List[int]]:
        for index in range(0,len(nums)+1):
            self.backtrack(0,list(),nums,index)
        return self.answer
    
if __name__=='__main__':
    ans=solution().subsets([0])
    print(ans)
            