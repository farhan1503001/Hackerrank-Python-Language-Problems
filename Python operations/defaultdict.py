from collections import defaultdict

if __name__=='__main__':
    dictionary=defaultdict(list)
    num_a,num_b=map(int,input().split())
    for i in range(num_a):
        dictionary[input().strip()].append(i)
    for j in range(num_b):
        value=input().strip()
        if value in dictionary:
            for index in dictionary[value]:
                print(index,end=' ')
            print()
        else:
            print(-1)