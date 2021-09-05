
class solution():
    def isBadVersion(self,version:int):
        return version>=4
    def firstBadVersion(self,n:int)->int:
        start=0
        end=n
        while(start<end):
            mid=start+(end-start)//2
            if not self.isBadVersion(mid):
                #no need to search left
                start=mid+1
            else:
                end=mid
        return start

if __name__=='__main__':
    print(solution().firstBadVersion(5))
