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
    defect_per,total_pin=map(float,input().split())
    defect_per=defect_per/100
    print(round(sum([binomial(total_pin,r,defect_per) for r in range(0,3)]),3))
    print(round(sum([binomial(total_pin,r,defect_per) for r in range(2,int(total_pin))]),3))