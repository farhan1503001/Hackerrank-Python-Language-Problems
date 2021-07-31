from collections import Counter


if __name__=='__main__':
    num_shoes=int(input().strip())
    shoes=list(map(int,input().split()))
    count_store=Counter(shoes)
    print(count_store)
    print(count_store.keys())
    print(count_store[5])
    print(count_store.values())
    num_customer=int(input().strip())
    sum=0
    for i in range(num_customer):
        size,price=map(int,input().split())
        if count_store[size]>0:
            sum+=price
            count_store[size]-=1
    
    print(sum)
