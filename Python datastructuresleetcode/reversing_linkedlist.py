class ListNode():
    def __init__(self,value) -> None:
        self.data=value
        self.next=None
class LinkedList():
    def __init__(self) -> None:
        self.head=None
    def create_linkedlist(self,arr:list)->ListNode:
        curr=None
        start=None
        for i in range(len(arr)):
            if i==0:
                curr=ListNode(arr[i])
                start=curr
            else:
                curr.next=ListNode(arr[i])
                curr=curr.next
        self.head=start
        return self.head
    def print_list(self,root:ListNode)->None:
        curr=root
        print()
        while(curr is not None):
            print(curr.data,end='  ')
            curr=curr.next
        
    def reverse_list(self)->ListNode:
        curr=self.head
        node=None
        while(curr is not None):
           temp=curr.next
           curr.next=node
           node=curr
           curr=temp
        self.head=node
        return node

if __name__=='__main__':
    linklist=LinkedList()
    root=linklist.create_linkedlist([1,4,5,6,7,2])
    linklist.print_list(root)
    new_head=linklist.reverse_list()
    linklist.print_list(new_head)
    new_head=linklist.reverse_list()
    linklist.print_list(new_head)

