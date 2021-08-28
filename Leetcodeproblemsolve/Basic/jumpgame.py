
from typing import List


class solution():
    def canjump(self,arr:List[int])->bool:
        m=len(arr)
        reached_distance=0
        is_possible=False
        for i in range(m):
            #hasnot reached yet
            if reached_distance<i:
                is_possible=False
                break
            reached_distance=max(reached_distance,arr[i]+i)
            print(reached_distance)
            if reached_distance>=m-1:
                is_possible=True
                break
        return is_possible


if __name__=='__main__':
    print(solution().canjump([2,3,1,1,4]))
    print(solution().canjump([3,2,1,0,4]))
    print(solution().canjump([0,1]))