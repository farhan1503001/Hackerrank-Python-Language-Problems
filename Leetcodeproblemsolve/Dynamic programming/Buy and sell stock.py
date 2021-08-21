
from typing import List

#maximizing the profit for stock market transactions 
# where only single transaction is permitted
class solution():
    def maxprofit(self,stocks:List[int])->int:
        """
        Target is to find minimum buying price and maximum profit(price-buyprice)
        """
        buying_price=float('inf')
        profit=0
        day1=-1
        day2=-1
        for i,price in enumerate(stocks):
            #Minimum buying price
            if buying_price>price:
                buying_price=price
                day1=i
            else:
                #if current profit is greater than only change profit
               if (price-buying_price)>profit:
                   profit=price-buying_price
                   day2=i
               else:
                   pass

        print(day1,day2)
        return profit
if __name__=='__main__':
    arr=[7,1,5,3,6,4]
    result=solution().maxprofit(arr)
    print(result)
