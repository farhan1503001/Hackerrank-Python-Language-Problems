class solution():
    def lcs(self,str1:str,str2:str)->int:
        '''
        if character of the two string matches then we will increase otherwise just till then maximum
        will be counted
        '''
        m=len(str1)+1
        n=len(str2)+1
        dp=[[0]*n]*m
        answer=0
        print(str1[3])
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if answer<dp[i][j]:
                    answer=dp[i][j]
        #temp=dp[m-1][n-1]
        print(dp)
        lister=list()
        i=m-1
        j=n-1
        while(i>0 and j>0):
            print(i,j)
            if str1[i-1]==str2[j-1]:
                lister.append(str2[j-1])
                i=i-1
                j=j-1
            elif dp[i-1][j]>dp[i][j-1]:
                i=i-1
            else:
                j=j-1 
        lister.reverse()
        print(lister)
        return answer



if __name__=='__main__':

    print(solution().lcs('abcba','abcbcba'))