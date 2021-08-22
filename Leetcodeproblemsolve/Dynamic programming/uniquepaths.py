#here is a robot on topleft of a grid
#we have to bring to bring it bottomright only down and right move possible 
#has to find the number of ways we can reach.
class solution():
    def uniquePaths(self,n:int,m:int)->int:
        #m and n are number of rows and columns respectively
        #first creating the grid
        dp=[[ 0 for y in range(m)] for x in range(n)]
        print(dp)
        #left and right first columns can be visited in a single way
        #'''''
        for i in range(n):
            dp[i][0]=1
        for j in range(m):
            dp[0][j]=1

        for iter1 in range(1,n):
            for iter2 in range(1,m):
                #top and same row immediate left
                dp[iter1][iter2]=dp[iter1-1][iter2]+dp[iter1][iter2-1]

        print(dp)
        return dp[-1][-1]
if __name__=='__main__':
    row=3
    col=3
    result=solution().uniquePaths(row,col)
    print(result)
