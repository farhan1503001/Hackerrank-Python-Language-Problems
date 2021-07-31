from collections import Counter
if __name__=='__main__':
    num=int(input().strip())
    arr=list(map(int,input().split()))
    mean=sum(arr)/len(arr)
    arr.sort()
    median= lambda num: arr[num//2] if num%2!=0 else (arr[num//2]+arr[num//2-1])/2
    countlist=Counter(arr)
    print(mean)
    print(median(num))
    print(countlist.most_common(1)[0][0])