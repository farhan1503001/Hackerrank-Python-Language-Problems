
class solution():
    def isPalindrome(self,n:int)->bool:
        if n<0 or (n%10==0 and n!=0):
            return False
        rev_num=0
        temp=n
        while(temp):
            rev_num=rev_num*10+(temp%10)
            temp=temp//10
        return n==rev_num
if __name__=='__main__':
    print(solution().isPalindrome(121))