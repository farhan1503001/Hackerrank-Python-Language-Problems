def unique(arr):
    uniquer=set(value for value in arr)
    print(uniquer)
    return float(sum(uniquer)/len(uniquer))

if __name__=='__main__':
  arr=list(map(int,input().split(' ')))
  print(arr)
  res=unique(arr)
  print(res)
