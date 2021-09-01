from typing import List


class solution():
    def findDuplicates(self,nums:List[int])->List[int]:
        memory=dict()
        result=list()
        for val in nums:
            if val not in memory:
                memory[val]=True
            else:
                if memory[val] is True:
                    result.append(val)
                    memory[val]=False
                else:
                    pass
        return result

if __name__=='__main__':
    print(solution().findDuplicates([4,3,2,7,8,2,3,1]))
