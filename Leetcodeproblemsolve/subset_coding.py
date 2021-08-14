from typing import List
class solution():
    def subset_finder(self,nums:List[int],answer:List[int],curr:List[int],index:int)->list:
        if index>len(nums):
            return
        #Appending what is curr value in answer here
        answer.append(curr[:])
        #Now iterating over index to final value
        for i in range(index,len(nums)):
            #check if the value already in curr to remove duplicacy
            if nums[i] not in curr:
                curr.append(nums[i])
                self.subset_finder(nums,answer,curr,i) #Recursive call to do again and again
                #after one call is finished pop top for next iteration
                curr.pop()
        
    def subsets(self,nums:List[int])->List[List[int]]:
        answer=[]
        curr=[]
        index=0
        self.subset_finder(nums,answer,curr,index)
        return answer

if __name__=='__main__':
    arr=[1,2,3]
    print(solution().subsets(arr))
