
class solution():
    def robbery(self,nums:list)->int:
        '''
        Args: nums list
        We will try to find out maximum amount a robber 
        can steal where he cannot steal from adjacen array
        '''
        number_elements=len(nums)
        if number_elements==0:
            return 0
        #Create a new array
        dp_result=[0]*number_elements
        #initial condition
        dp_result[0]=nums[0]
        #Due to choosing option
        dp_result[1]=max(nums[0],nums[1])
        for i in range(2,number_elements):
            #previous two index i-1 if he doesnot steal i
            dp_result[i]=max(dp_result[i-1],dp_result[i-2]+nums[i])

        #print([value for value in dp_result])

        return dp_result[-1]

if __name__=='__main__':
    arr=[1,2,3,1]
    print(solution().robbery(arr))