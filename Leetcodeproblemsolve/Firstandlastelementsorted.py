class solution():
    def find_left_element(self,arr:list,target:int)->int:
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target and (mid==0 or arr[mid-1]<target and mid-1>=0):
                return mid
            elif arr[mid]>=target:
                high=mid-1
            else:
                low=mid+1
        return -1
    def find_right_element(self,arr:list,target:int)->int:
        low=0
        high=len(arr)-1
        while(low<high):
            mid=(low+high)//2
            if arr[mid]==target and (arr[mid+1]>target or mid==len(arr)-1):
                return mid
            if target>=arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1

    def search_range(self,arr:list,target:int)->list:
        left=self.find_left_element(arr,target)
        right=None
        if left!=-1:
            right_arr=arr[left+1:]
            right=self.find_right_element(right_arr,target)
        return [left,left+right+1]
if __name__=='__main__':
    sol=solution()
    arr=[5,5,5,5,5,7,8,9]
    print(sol.search_range(arr,5))