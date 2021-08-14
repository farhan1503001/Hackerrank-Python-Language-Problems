from typing import List
class solution():
    def find_zeros(self,arr:List[int])->List[int]:
        position=0
        length=len(arr)
        for value in arr:
            if value!=0:
                arr[position]=value
                position+=1
        print(position)
        for i in range(position,length):
            arr[i]=0
        return arr
if __name__=='__main__':
    array=[0,1,0,3,12]
    print(solution().find_zeros(array))
