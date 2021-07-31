if __name__=='__main__':
    num,store=int(input().strip()),input().split()
    res=all([int(val)>=0 for val in store ])
    cond=any(val==val[::-1] for val in store)
    print(res and cond)