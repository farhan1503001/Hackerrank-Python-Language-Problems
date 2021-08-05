import math
if __name__=='__main__':
    size=int(input().strip())
    X=list(map(float,input().split()))
    Y=list(map(float,input().split()))
    avg=lambda x: sum(x)/len(x)
    sq_deviated=lambda arr: math.sqrt(sum([(value-avg(arr))**2 for value in arr])/len(arr))
    correlation=sum([(x-avg(X))*(y-avg(X))for x,y in zip(X,Y)])/(size*sq_deviated(X)*sq_deviated(Y))
    print(round(correlation,3))