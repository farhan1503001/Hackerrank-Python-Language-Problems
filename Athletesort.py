
if __name__=='__main__':
    m,n=map(int,input().split())
    athlets=list()
    for _ in range(m):
        athlets.append(list(map(int,input().split())))

    k=int(input().strip())
    athlets.sort(key=lambda x:x[k])
    for athlet in athlets:
        print(*athlet,sep=' ')
