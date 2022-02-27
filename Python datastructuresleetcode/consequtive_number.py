
from cgitb import small


def consequtive_number(a:int,b:int,c:int)->bool:
    #First try to find out smallest number among them:
    smallest=None
    if a<b and a<c:
        smallest=a
    elif b<a and b<c:
        smallest=b
    else:
        smallest=c
    
    #print(smallest)
    sub1=a-smallest
    sub2=b-smallest
    sub3=c-smallest
    
    zero_flag=False
    one_flag=False
    two_flag=False
    #checking zero_flag
    if sub1==0 or sub2==0 or sub3==0:
        zero_flag=True
    if sub1==1 or sub2==1 or sub3==1:
        one_flag=True
    if sub1==2 or sub2==2 or sub3==2:
        two_flag=True
    #Now return
    if zero_flag==True and one_flag==True and two_flag==True:
        return True
    else:
        return False
    
if __name__=='__main__':
    print(consequtive_number(2,4,3))