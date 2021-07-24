if __name__=='__main__':
    a=set(input().split())
    print(a)
    n=int(input().strip())
    count=0
    for i in range(n):
        b=set(input().split())
        print(b)
        if a.issuperset(b):
            count+=1
    print(count==n)
    ''''
    for i in input:
        print(i)
    '''