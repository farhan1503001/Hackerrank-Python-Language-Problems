from typing import List
class solution():
    def quick_sort(self,arr:List[int],start:int,end:int)->None:
        if start<end:
            mid=self.partition(arr,start,end)
            #print(mid)
            #print(arr)
            self.quick_sort(arr,start,mid-1)
            self.quick_sort(arr,mid+1,end)
    def partition(self,arr:List[int],start:int,end:int)->int:
        i=start-1
        j=start
        pivot_value=arr[end]
        while(j<=end):
            if arr[j]<=pivot_value:
                i+=1
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
            j+=1
        return i
if __name__=='__main__':
    input_array=[10,7,1,3,5,8,9,6]
    solution().quick_sort(input_array,0,len(input_array)-1)
    print(input_array)
