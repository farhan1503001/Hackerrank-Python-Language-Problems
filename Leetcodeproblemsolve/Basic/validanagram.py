class solution():
    def validAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        dictionary=[0 for _ in range(26)]
        for i in range(len(s)):
            dictionary[ord(s[i])-ord('a')]+=1
            dictionary[ord(t[i])-ord('a')]-=1
        
        for val in dictionary:
            if val!=0:
                return False
        return True

if __name__=='__main__':
    print(solution().validAnagram('anagram','naaramg'))
            