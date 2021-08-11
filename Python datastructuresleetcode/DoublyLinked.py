class node:
    def __init__(self,value:int) -> None:
        self.data=value
        self.prev=None
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def create_list(self,arr)->None:
        number=len(arr)
        start=self.head
        for i in range(number):
            newnode=node(arr[i])
            if i==0:
                start=newnode
                curr=start
            else:
                temp=curr
                curr.next=newnode
                curr=curr.next
                curr.prev=temp
        self.head=start
        self.tail=curr
    def print_list(self)->None:
        curr=self.head
        print()
        while(curr is not None):
            print(curr.data,end='  ')
            curr=curr.next
    def back_print(self)->None:
        curr=self.tail
        print()
        while(curr is not None):
            print(curr.data,end='   ')
            curr=curr.prev
    def countlist(self)->int:
        curr=self.head
        count=0
        while(curr is not None):
            count+=1
            curr=curr.next
        return count
            
    def insert_at_location(self,value,index)->None:
        curr=self.head
        length=self.countlist()
        if index>length+1:
            return curr
        if index==1:
            newnode=node(value)
            newnode.next=curr
            curr.prev=newnode
            self.head=newnode
            return self.head
        elif index==length+1:
            while(curr.next is not None):
                curr=curr.next
            temp=curr
            curr.next=node(value)
            curr=curr.next
            curr.prev=temp
            self.tail=curr
            return self.head
        else:
            count=1
            while(count!=index-1):
                curr=curr.next
                count+=1
            newnode=node(value)
            temp=curr.next
            temp1=curr
            curr.next=newnode
            curr=curr.next
            curr.next=temp
            curr.prev=temp1
            self.tail=curr
            return self.head


if __name__=='__main__':
    arr=[1,2,3,4,5]
    linklist=LinkedList()
    linklist.create_list(arr)
    linklist.print_list()
    linklist.back_print()
    linklist.insert_at_location(5,6)
    linklist.print_list()
    linklist.back_print()
