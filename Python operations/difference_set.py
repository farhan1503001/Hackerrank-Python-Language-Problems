if __name__=='__main__':
    num=int(input().strip())
    set_a=set(map(int,input().split()))
    num1=int(input().strip())
    set_b=set(map(int,input().split()))
    print(len(set_a.difference(set_b)))