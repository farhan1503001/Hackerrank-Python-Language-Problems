import math
class solution():
    def countPrimes(self,n:int)->int:
        #suppose all are true
        sieve_array=[True]*(n+1)
        sieve_array[0]=sieve_array[1]=False
        sqrt_n=math.ceil(math.sqrt(n))
        i=2
        while(i<=sqrt_n):
            if sieve_array[i]:
                j=2
                while(j*i<=n):
                    sieve_array[j*i]=False
                    j+=1
            i+=1
        count=0
        for num in range(2,n):
            if sieve_array[num]:
                count+=1
        return count

if __name__=='__main__':
    print(solution().countPrimes(10))