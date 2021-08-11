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
    def merge_sort_linkedlist(self,l1:ListNode,l2:ListNode)->ListNode:
        curr=ListNode(0)
        ans=curr
        while(l1 and l2):

            if l1.data<=l2.data:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        while(l1):
            curr.next=l1
            curr=curr.next
            l1=l1.next
        while(l2):
            curr.next=l2
            curr=curr.next
            l2=l2.next
        return ans.next
    def print_linklist(self,root:ListNode)->None:
        curr=root
        while(curr is not None):
            print(curr.data,end=' ')
            curr=curr.next
if __name__=='__main__':
    linkedlist=LinkedList()
    l1=linkedlist.create_list([1,3,4,5,7])
    l2=linkedlist.create_list([1,2,3,8,9,10])
    sol=solution()
    n_head=sol.merge_sort_linkedlist(l1,l2)
    sol.print_linklist(n_head)