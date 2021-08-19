class heappy():
    def __init__(self,size:int) -> None:
        self.size=0
        self.max_size=size
        self.heap_array=list()
    def is_full(self)->bool:
        return self.size==self.max_size
    def is_empty(self)->bool:
        return self.size==0
    def get_parent(self,index:int)->int:
        return int((index-1)/2)
    def get_child(self,index:int,left:bool)->int:
        return 2*index+ 1 if left else 2
    def __fixaboveheap(self,index:int)->None:
        newvalue=self.heap_array[index]
        curr_index=index
        while(curr_index>0 and newvalue>self.heap_array[self.get_parent(curr_index)]):
            self.heap_array[curr_index]=self.heap_array[self.get_parent(curr_index)]
            curr_index=self.get_parent(curr_index)
        self.heap_array[curr_index]=newvalue
    def insert_heap(self,value:int)->None:
        if self.is_full():
            raise IndexError("Max heap is full")
        self.heap_array.append(value)
        self.__fixaboveheap(self.size)
        self.size+=1
    def delete_heap(self,index=0)->int:
        if self.is_empty():
            raise IndexError("Heap is empty!")
        deleted_value=self.heap_array[index]
        self.heap_array[index]=self.heap_array[self.size-1]
        if index==0 or self.heap_array[index]<self.heap_array[self.get_parent(index)]:
            self.__fixbelow(index,self.size-1)
        else:
            self.__fixaboveheap(index)
        self.size-=1
        return deleted_value
    def __fixbelow(self,index:int,last_element:int)->None:
        curr_index=index
        swap_child=None
        while(curr_index<=last_element):
            left=self.get_child(curr_index,True)
            right=self.get_child(curr_index,False)
            if left<=last_element:
                if right>last_element:
                    swap_child=left
                else:
                    swap_child=left if self.heap_array[left]>self.heap_array[right] else right
                if(self.heap_array[swap_child]>self.heap_array[curr_index]):
                    temp=self.heap_array[swap_child]
                    self.heap_array[swap_child]=self.heap_array[curr_index]
                    self.heap_array[curr_index]=temp
                else:
                    break
                curr_index=swap_child        
            else:
                break
    def heap_sort(self)->list:
        sorted_numlist=list()
        while(not self.is_empty()):
            value=self.delete_heap()
            print(value,end=" ")
            sorted_numlist.append(value)
    def peek(self):
        if self.heap_array is None:
            raise IndexError("Heap is empty")
        else:
            return self.heap_array[0]
    def print_heap(self):
        print()
        for value in self.heap_array:
            print(value,end='\t')



if __name__=='__main__':
    heap=heappy(10)
    #print(heap.peek())
    arr=[80,75,60,68,55,40,52,67]
    [heap.insert_heap(value) for value in arr]
    heap.print_heap()
    heap.delete_heap()
    print(heap.peek())
    heap.print_heap()
    heap.heap_sort()
    
