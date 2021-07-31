
def sym_diff(arr1,arr2):
    f1=set.difference(arr1,arr2)
    f2=set.difference(arr2,arr1)
    #Adding two sets
    print(f1)
    print(f2)
    un=list(set.union(f1,f2))
    un.sort()
    for value in un:
        print(value)


if __name__=='__main__':
    n=int(input().strip())
    arr1=set(list(map(int,input().split())))
    m=int(input().strip())
    arr2=set(list(map(int,input().split())))
    sym_diff(arr1,arr2)