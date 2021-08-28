
class solution():
    def isMatch(self,string:str,pattern:str):
        """
        we have to match prev_el of * also either any character or match with pattern
        """
        m=len(string)
        n=len(pattern)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True
        #special case handeling
        for col in range(1,n+1):
            if pattern[col-1]=='*':
                dp[0][col]=dp[0][col-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                #if both matches or any character
                if pattern[j-1]=='.' or string[i-1]==pattern[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif pattern[j-1]=='*':
                    dp[i][j]=dp[i][j-2]
                    #check if prev is matching our current character or any char
                    if pattern[j-2]==string[i-1] or pattern[j-2]=='.':
                        dp[i][j]=dp[i][j] or dp[i-1][j]
                    else:
                        dp[i][j]=False
        return dp[m][n]

if __name__=='__main__':
    print(solution().isMatch("axyb","a.*b"))
        