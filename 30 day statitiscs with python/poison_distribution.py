import math
if __name__=='__main__':
    #poison distribution p(k)=lambda**k*e-lambda/k!
    average=float(input().strip())
    k=float(input().strip())
    result=((average**k)*(math.exp(-average)))/math.factorial(k)
    print(result)
