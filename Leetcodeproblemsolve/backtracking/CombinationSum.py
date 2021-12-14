from typing import List
class solution():
    #here candidates mane next e kara kara ache
    def backtrack(self,target:int,currents:List[int],candidates:List[int],start:int,results:List[List[int]]):
        if target==0:
            results.append(currents.copy())
            return
        if target<0:
            return
        for i in range(start,len(candidates)):
            #protteker jonno ekta tree toiri hobe
            currents.append(candidates[i])
            self.backtrack(target-candidates[i],currents,candidates,i,results)
            currents.pop()
            
        
    def combinationsum(self,arr:List[int],target:int)->List[List[int]]:
        #here we will substract and stop operation when it is equal to zero
        #ekhane current sum thakbe sei list
        currents=list()
        results=list()
        self.backtrack(target,currents,arr,0,results)
        return results
    
if __name__=='__main__':
    results=solution().combinationsum([2,3,5],8)
    print(results)