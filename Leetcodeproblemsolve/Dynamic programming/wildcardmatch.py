
class solution():
    def wildcardmatch(self,string:str,pattern:str):
        """
        ? means any character so it is a match
        * means any sequence means previous and taking
        """
        #first find the lengths
        m=len(string)
        n=len(pattern)
        #create a dp array with column=pattern and row=string
        dp=[[False]*(n+1) for _ in  range(m+1) ]
        #select the first value as dp[0][0]=true
        dp[0][0]=True
        #For handeling special cases
        for col in range(1,n+1):
            if pattern[col-1]=='*':
                dp[0][col]=dp[0][col-1]
        #Now iteration
        for i in range(1,m+1):
            for j in range(1,n+1):
                if string[i-1]==pattern[j-1] or pattern[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif pattern[j-1]=='*':
                    #two choice match a?bc with string or abc abc
                    dp[i][j]=dp[i-1][j] or dp[i][j-1] #any match if pattern then yes
                else:
                    dp[i][j]=False
        
        return dp[m][n]

if __name__=='__main__':
    print(solution().wildcardmatch("abcdef","a?c*f"))