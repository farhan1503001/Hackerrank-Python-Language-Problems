
class solution():
    def isSubsequence(self,s:str,t:str)->bool:
        if s is None:
            return True
        match_pointer=0
        i=0
        size=len(t)
        while(i<size):
            #match found move pointer
            if s[match_pointer]==t[i]:
                print(s[match_pointer],t[i])
                match_pointer=match_pointer+1
            i=i+1
        return match_pointer==len(s)

if __name__=='__main__':
    print(solution().isSubsequence("abc","ahbgdc"))
    print(solution().isSubsequence("axc","ahbgdc"))
