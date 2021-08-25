from typing import List


class solution():
    def fizzbuzz(self,n:int)->List[str]:
        num_store=list()
        for i in range(1,n+1):
            arbitary=''
            if i%3==0:
                arbitary+='Fizz'
            if i%5==0:
                arbitary+='Buzz'
            if arbitary=='':
                num_store.append(str(i))
            else:
                num_store.append(arbitary)
        return num_store

if __name__=='__main__':
    print(solution().fizzbuzz(6))