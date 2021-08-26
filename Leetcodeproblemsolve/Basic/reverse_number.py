class solution():
    def reverse_number(self,x:int)->int:
        
        number= x*-1 if x<0 else x
        rev=0
        while(number):
            rev=rev*10+(number%10)
            number=number//10
        if rev>=(2**31-1) or rev<=(-2**31):
            return 0
        return rev*-1 if x<0 else rev

if __name__=='__main__':
    print(solution().reverse_number(1534236469))
        
        