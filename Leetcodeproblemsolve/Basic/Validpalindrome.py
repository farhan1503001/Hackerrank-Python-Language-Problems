class solution():
    def isPalindrom(self,s:str)->bool:
        i=0
        j=len(s)-1
        palindrome_status=True
        while(i<=j):
            if s[i].isalnum()==False:
                i=i+1
            elif s[j].isalnum()==False:
                j=j-1
            else:
                if s[i].lower()!=s[j].lower():
                    palindrome_status=False
                    break
                else:
                    i+=1
                    j-=1
        return palindrome_status

if __name__=='__main__':
    print(solution().isPalindrom("A man, a plan, a canal: Panama"))
