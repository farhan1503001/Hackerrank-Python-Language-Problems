from itertools import combinations

if __name__=='__main__':
    word,k=input().split()
    k=int(k)
    for i in range(1,k+1):
        groups=list(combinations(sorted(word),r=i))
        groups.sort()
        [print(''.join(val)) for val in groups]

