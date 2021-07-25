if __name__=='__main__':
    n=int(input().strip())
    arr=list(map(int,input().split()))
    #print(max(arr))
    winner=max(arr)
    while max(arr)==winner:
        arr.remove(max(arr))
    print(max(arr))