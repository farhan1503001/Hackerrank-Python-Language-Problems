class solution():
   def majority_problem(self,arr:list)->None:
       memory=dict()
       for value in arr:
           if value not in memory:
               memory[value]=1
           else:
                memory[value]+=1
       return [key for key,val in memory.items() if val>len(arr)//2][0]

if __name__=='__main__':
    arr=[1,2,3,1,1]
    sol=solution()
    print(sol.majority_problem(arr))
    #print(solution().majority_problem(arr))
