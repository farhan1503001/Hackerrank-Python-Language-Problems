
from typing import List

class solution():
    def wordBreak(self,s:str,wordDict: List[str])->bool:
        #creating a dp array
        dp=[False]*(len(s)+1)
        #for handeling repeating words
        word_set=set(wordDict)
        dp[0]=True
        #this loop will iterate through limit string
        for i in range(len(s)+1):
            for j in range(i):
                print(s[j:i])
                if dp[j]==True and s[j:i] in  word_set:
                    print("String Found "+s[j:i])
                    dp[i]=True
                    #now break inner loop
                    break
        return dp[len(s)]

if __name__=='__main__':
    print(solution().wordBreak("leetcode",['leet','code']))
    print()
    print(solution().wordBreak("catsandog",["cats","dog","sand","and","cat"]))
