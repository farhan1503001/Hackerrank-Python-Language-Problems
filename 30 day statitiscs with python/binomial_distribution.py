def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))
def binomial(n,r,p):
    return combination(n,r)*(p**r)*((1-p)**(n-r))
if __name__=='__main__':
    l,r=map(float,input().split())
    odds=l/r
    result=sum([binomial(6,r,odds/(1+odds)) for r in range(3,7)])
    print(round(result,3))
    