from math import sqrt
if __name__=='__main__':
    size=int(input().strip())
    arr=list(map(int,input().split()))
    avg= lambda size: sum(arr)/size
    sq_deviated= sqrt(sum([(x-avg(size))**2 for x in arr])/size)
    print(round(sq_deviated,1))
