
if __name__=='__main__':
    n=int(input().strip())
    X=list(map(float,input().split()))
    Y=list(map(float,input().split()))    
    rankmaker=lambda arr: {value:index for index,value in enumerate(sorted(arr))}
    rank_x=rankmaker(X)
    rank_y=rankmaker(Y)
    #print(rank_x)
    #print(rank_y)
    dsq=sum([(rank_x[x]-rank_y[y])**2 for x,y in zip(X,Y)])
    rxy=1-((6*dsq)/(n*(n**2-1)))
    print(round(rxy,3))