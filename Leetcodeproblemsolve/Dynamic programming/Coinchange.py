"""
Target of this solution is to find minimum number of coins to compose an amount
"""
from typing import List

class solution():
    def coinchange(self,coins:List[int],amount:int)->int:
        if amount<=0:
            return 0
        #check if possible from begininng
        if min(coins)>amount:
            return -1 #cannot be solved
        
        constant=int(99999999999)
        #Now dp array to hold results:
        dp_arr=[constant]*(amount+1) #will start indexing from 1
        dp_arr[0]=0
        for curr_money in range(1,amount+1):
            for coin in coins:
                if coin<=curr_money:
                    dp_arr[curr_money]=min(dp_arr[curr_money],dp_arr[curr_money-coin]+1)
        print([value for value in dp_arr])

        return dp_arr[amount] if dp_arr[amount]!=constant else -1

if __name__=='__main__':
    coins=[1,2,5]
    amount=11
    res=solution().coinchange(coins,amount)
    print(res)

