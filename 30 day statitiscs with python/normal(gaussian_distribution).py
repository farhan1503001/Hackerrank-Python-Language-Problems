import math
if __name__=="__main__":
    mean,std=map(float,input().split())
    term_bound=float(input().strip())
    boundary1,boundary2=map(float,input().split())
    ##probablity x suggests for probablity for less than equal to x
    cdf=lambda value: (1+math.erf((value-mean)/(math.sqrt(2)*std)))*0.5
    print(cdf(term_bound))
    print(cdf(boundary2)-cdf(boundary1))