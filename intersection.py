if __name__=='__main__':
    num_a=input().strip()
    set_a=set(map(int,input().split()))
    num_b=input().strip()
    set_b=set(map(int,input().split()))
    print(len(set_a.intersection(set_b)))