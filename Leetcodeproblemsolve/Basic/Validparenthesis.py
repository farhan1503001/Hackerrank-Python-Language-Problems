
class solution():
    def isValid(self,s:str)->bool:
        if not s:
            return True
        if len(s)<=1:
            return False
        memoy={')':'(','}':'{',']':'['}
        stack=list()
        for char in s:
            if char not in memoy:
                stack.append(char)
            else:
                if stack:
                    val=stack.pop()
                    if memoy[char]!=val:
                        return False
                    else:
                        pass
                else:
                    return False
        return True if len(stack)<=0 else False

if __name__=='__main__':
    print(solution().isValid('()[]'))