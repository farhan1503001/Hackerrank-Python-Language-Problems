
from typing import List


class solution():
    def backtrack(self,answer:List[str],text:str,open:int,close:int,max:int):
        if len(text)==2*max:
            answer.append(text)
            return
        if open<max:
            self.backtrack(answer,text+"(",open+1,close,max)
        if close<open:
            self.backtrack(answer,text+")",open,close+1,max)
    def GenerateParenthesis(self,n:int)->List[str]:
        answer=list()
        self.backtrack(answer,"",0,0,n)
        return answer

if __name__=='__main__':
    answer=solution().GenerateParenthesis(3)
    print(answer)

