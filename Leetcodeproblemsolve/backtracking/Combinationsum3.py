from typing import List
class solution():
    def backtrack(self,remain:int,size:int,currents:List[int],next_element:int,results:List[List[int]])->None:
        '''
        remain->mane koto baki ache ta bojhabe
        size->list er size bojhabe
        currents:combination k hold korbe
        next element->porer element er dike jabe
        results->result ke hold korbe
        '''
        if remain==0 and len(currents)==size:
            results.append(currents.copy())
            return
        if remain<0 or len(currents)==size:
            return
        for index in range(next_element,9):
            #porer take send korbo upore mane 1 er jonno 2,3,4,5 ek dorkar nai
            currents.append(index+1)
            self.backtrack(remain-index-1,size,currents,index+1,results)
            currents.pop()
        
    def combinationsum3(self,size_len:int,target:int)->List[List[int]]:
        #ekhane size_len mane koto sonkhar combination chai ami
        #ekhane target mane combination er sum koto hote hobe
        currents=list()#combination dhore rakhbe
        results=list()#final result store rakhbe
        self.backtrack(target,size_len,currents,0,results)
        return results
    
if __name__=='__main__':
    results=solution().combinationsum3(3,9)
    print(results)
        