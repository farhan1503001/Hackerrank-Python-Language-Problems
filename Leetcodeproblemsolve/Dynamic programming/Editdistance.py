
class solution():
    def edit_distance(self,text1:str,text2:str)->int:
        '''
        if upper row of grid will be main string1 lower part will be
        string2 we will try to find how many string conversion are required to make 
        that part
        '''
        len_1=len(text1)
        len_2=len(text2)
        #memory array 2d
        dp=[[0]*(len_1+1) for i in range(len_2+1)]
        print(dp)
        for i in range(0,len_1+1):
            dp[0][i]=i
        for j in range(0,len_2+1):
            dp[j][0]=j
        for i in range(1,len_2+1):
            for j in range(1,len_1+1):
                if text2[i-1]==text1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    temp=min(min(dp[i-1][j-1],dp[i-1][j]),dp[i][j-1])
                    dp[i][j]=temp+1
        print(dp[i][j])
        print(dp)

if __name__=='__main__':
    solution().edit_distance('abdceg','agcef')