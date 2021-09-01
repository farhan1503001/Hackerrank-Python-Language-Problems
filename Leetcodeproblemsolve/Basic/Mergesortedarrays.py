from typing import List
class solution():
    def merge(self,nums1:List[int],m:int,nums2:List[int],n:int)->None:
        """
        nums1=[1,2,3,0,0,0]
        nums2=[2,5,6] have to sort them inorder will start from last one for this
        particular case
        """
        #mandn are size so indexisize them
        if n==0:
            print(nums1)
            return
        if m==0:
            nums1[:]=nums2
            print(nums1)
            return
        point_array1=m-1
        point_array2=n-1
        index=len(nums1)-1
        while(point_array1>=0 and point_array2>=0):
            if nums1[point_array1]>nums2[point_array2]:
                nums1[index]=nums1[point_array1]
                point_array1-=1
            else:
                nums1[index]=nums2[point_array2]
                point_array2-=1
            index-=1
        while point_array2>=0:
            nums1[index]=nums2[point_array2]
            point_array2-=1
            index-=1
        print(nums1)

if __name__=='__main__':
    solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    solution().merge([0],0,[1],1)
    solution().merge([2,0],1,[1],1)
