class ListNode:
    def __init__(self,value:int) -> None:
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def create_list(self,arr:list)->ListNode:
        number=len(arr)
        start=self.head
        for i in range(number):
            newnode=ListNode(arr[i])
            if i==0:
                start=newnode
                curr=start
            else:
                curr.next=newnode
                curr=curr.next
        self.head=start
        return self.head
class solution:
    def add_two_numbers(self,l1:ListNode,l2:ListNode)->ListNode:
        '''
         3 2 1
         4 5 2
         7 7 3 result is 377
         Args:
            ListNode: l1 and l2
         Returns:
            ListNode: head of new list
        '''
        answer=ListNode(0)
        pointer=answer
        sum=0
        carry=0
        while(l1!=None or l2!=None):
            sum=carry #Extra addition at first 0
            if l1 is not None:
                sum+=l1.data
                l1=l1.next
            if l2 is not None:
                sum+=l2.data
                l2=l2.next
            carry=int(sum/10)
            pointer.next=ListNode(sum%10)
            pointer=pointer.next
            sum=carry
        #Overflow occurs
        if(carry):
            pointer.next=ListNode(carry)
        return answer.next
    def print_linklist(self,root:ListNode)->None:
        curr=root
        while(curr):
            print(curr.data,end='  ')
            curr=curr.next

if __name__=='__main__':
    linkedlist=LinkedList()
    l1=linkedlist.create_list([2,4,3])
    l2=linkedlist.create_list([5,6,4])
    sol=solution()
    n_head=sol.add_two_numbers(l1,l2)
    sol.print_linklist(n_head)
