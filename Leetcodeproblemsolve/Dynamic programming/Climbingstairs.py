#Goal of this programm is to find out in how many ways
#one can reach nth stair it's a dp problem
class solution():
    def climb_stairs(self,n:int)->int:
        if n==1:
            return 1 #if step is 1 only one way we can reach
        else:
            #create a dp array
            dp=[0]*(n+1)#6th stair 
            #Assigning initials
            dp[1]=1
            dp[2]=2
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            
            print([value for value in dp])

        return dp[n]

if __name__=='__main__':
    n=6
    result=solution().climb_stairs(n)
    print(result)