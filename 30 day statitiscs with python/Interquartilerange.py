def median(arr):
    size=len(arr)
    if size%2!=0:
        return arr[size//2]
    else:
        return (arr[size//2]+arr[size//2-1])/2.0
import statistics as st
if __name__=='__main__':
    num=int(input().strip())
    values=list(map(int,input().split()))
    freq=list(map(int,input().split()))
    final_values=[[value]*f for value,f in zip(values,freq)]
    final_values=[value for sub in final_values for value in sub]
    #print(final_values)
    
    final_values.sort()
    if num%2==0:
        first=final_values[:len(final_values)//2]
        second=final_values[len(final_values)//2:]
    else:
        first=final_values[:len(final_values)//2]
        second=final_values[len(final_values)//2+1:]
    #print(first)
    #print(second)
    res=median(second)-median(first)
    print(round(float(res),1))