
from typing import List


class solution():
    def sequentialDigits(self,low:int,high:int)->List[int]:
        """
        we will find sequential digit of every possible size if it 
        falls withing low and high limit then add it to result
        """
        #sorted digits 
        digits="123456789"
        result=list()
        for size in range(1,len(digits)):
            j=0
            while j<len(digits)-size:
                print(size,j)
                val=int(digits[j:j+size])
                if val>=low and val<=high:
                    result.append(val)
                j+=1
        print(result)
        return result

if __name__=='__main__':
    solution().sequentialDigits(1000,13000)



