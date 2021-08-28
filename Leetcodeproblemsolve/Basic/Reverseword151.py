class solution():
    def reverseword(self,s:str)->str:
        s=s.rstrip().lstrip().split()
        print(s)
        return ' '.join([s[index] for index in range(len(s)-1,-1,-1)])
if __name__=='__main__':
    print(solution().reverseword("My name is lakkhan"))
    print(solution().reverseword("  hello world  "))
    print(solution().reverseword("a good   example"))
