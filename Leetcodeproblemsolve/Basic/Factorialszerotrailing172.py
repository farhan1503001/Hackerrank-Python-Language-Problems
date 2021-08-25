
class solution():
    def factorials_trailing_zeroes(self,n:int)->int:
        '''
        finding the number of occurance of five as number of
        five equates to 10 which then results in zeros
        '''
        counter=0
        while(n):
            n=n//5
            counter+=1
        #print(counter)
        return counter

if __name__=='__main__':
    print(solution().factorials_trailing_zeroes(12))