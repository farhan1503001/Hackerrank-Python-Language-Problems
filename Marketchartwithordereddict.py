from collections import OrderedDict

if __name__=='__main__':
    market=OrderedDict()
    num=int(input().strip())
    for _ in range(num):
        lister=input().split()
        num=int(lister[-1])
        key=' '.join(lister[:-1])
        if market.get(key):
            market[key]+=num
        else:
            market[key]=num
    for key,value in market.items():
        print(key,value)