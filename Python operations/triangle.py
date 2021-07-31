if __name__=='__main__':
    num=int(input().strip())
    for i in range(1,num):
        for j in range(i):
            print(i,end='')
        print()
    for i in range(1,num):
        res=(pow(10,i)//9)*i
        print(res)