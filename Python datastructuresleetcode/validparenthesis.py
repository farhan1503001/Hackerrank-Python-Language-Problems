class stack():
    def __init__(self) -> None:
        self.st=list()
    def push(self,value:int)->None:
        self.st.append(value)
    def top(self)->int:
        return self.st[-1] if self.st else None
    def pop(self)->None:
        if self.st:
            self.st.pop()
    def is_empty(self)->bool:
        return len(self.st)==0
class solution():
    def is_equal(self,char1:str,char2:str)->bool:
        if char1 =='(' and char2==')':
            return True
        elif char1=='{' and char2=='}':
            return True
        elif char1=='[' and char2==']':
            return True
        else:
            return False

    def valid_parenthis(self,string:str)->bool:
        st=stack()
        for chr in string:
            curr=st.top()
            if self.is_equal(curr,chr):
                st.pop()
                continue
            st.push(chr)
        return st.is_empty()

if __name__=='__main__':
    string=input().strip()
    sol=solution()
    print(sol.valid_parenthis(string))
        