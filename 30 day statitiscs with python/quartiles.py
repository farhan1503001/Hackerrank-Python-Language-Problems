def median(arr):
    size=len(arr)
    if(size%2!=0):
        return arr[size//2]
    else:
        return (arr[size//2]+arr[size//2-1])//2
    return
if __name__=='__main__':
    n=int(input().strip())
    values=list(map(int,input().split()))
    values.sort()
    if len(values)%2==0:
        firsthalf=values[:len(values)//2]
        secondhalf=values[len(values)//2:]
    else:
        firsthalf=values[:len(values)//2]
        secondhalf=values[len(values)//2+1:]
    ''''
    print(firsthalf)
    print(secondhalf)
    print(values)
    '''
    print(median(firsthalf))
    print(median(values))
    print(median(secondhalf))