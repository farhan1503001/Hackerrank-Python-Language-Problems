if __name__=='__main__':
    n=int(input().strip())
    values=list(map(int,input().split()))
    weights=list(map(int,input().split()))
    result=[value*weight for value,weight in zip(values,weights)]
    print(round(sum(result)/sum(weights),1))