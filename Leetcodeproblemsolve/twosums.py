
class solution():
    def two_sums(self,arr:list,target:int)->list:
        memory=dict()
        for index,value in enumerate(arr):
            temp=target-value
            print(temp)
            if temp in memory:
                return [memory[temp],index]
            memory[value]=index
        '''''
        for key,value in memory.items():
            print(key,value)
        '''

if __name__=='__main__':
    arr=[3,6,12,14]
    target=15
    print([(index,value) for index,value in enumerate(arr)])
    print(solution().two_sums(arr,target))
