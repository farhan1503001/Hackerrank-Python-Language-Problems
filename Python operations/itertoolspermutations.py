from itertools import permutations

if __name__=='__main__':
    word,k=input().split()
    k=int(k)
    variations=list(permutations(word,r=k))
    variations.sort()
    [print("".join(val))for val in variations]