class Minheap():
    def __init__(self,size) -> None:
        self.maxsize=size
        self.heap_array=list()
        self.size=0
    def is_full(self):
        return self.size==self.maxsize
    def is_empty(self):
        return self.size==0
    def is_full(self)->bool:
        return self.size==self.maxsize
    def is_empty(self)->bool:
        return self.size==0
    def get_parent(self,index:int)->int:
        return int((index-1)/2)
    def get_child(self,index:int,left:bool)->int:
        return 2*index+ 1 if left else 2
    def insert(self,value:int)->None:
        if self.is_full():
            raise IndexError("Heap is full")
        else:
            self.heap_array.append(value)
            self.__fixheapabove()
            self.size+=1
    def __fixheapabove(self):
        index=self.size-1
        curr_value=self.heap_array[index]
        while(curr_value<self.heap_array[self.get_parent(index)] and index>0):
            self.heap_array[index]=self.heap_array[self.get_parent(index)]
            index=self.get_parent(index)
        self.heap_array[index]=curr_value
    def delete(self,index:int=0)->int:
        if self.is_empty():
            raise IndexError("Empty Heap")
        deleted_value=self.heap_array[index]
        self.heap_array[index]=self.heap_array[self.size-1]
        if index==0 or self.heap_array[index]>self.heap_array[self.get_parent(index)]:
            self.__fixheapbelow(index,self.size-1)
        else:
            self.__fixheapabove()
        self.size-=1
        return deleted_value
    def __fixheapbelow(self,index:int,lastelement:int)->None:
        curr_index=index
        swapchild=None
        while(curr_index<=lastelement):
            left=self.get_child(curr_index,True)
            right=self.get_child(curr_index,False)
            if left<=lastelement:
                if right>lastelement:
                    swapchild=left
                else:
                    swapchild=left if self.heap_array[left]<self.heap_array[right] else right
                if(self.heap_array[swapchild]<self.heap_array[curr_index]):
                    temp=self.heap_array[swapchild]
                    self.heap_array[swapchild]=self.heap_array[curr_index]
                    self.heap_array[curr_index]=temp
                else:
                    break
                curr_index=swapchild
            else:
                break
    def heap_sort(self)->list:
        lister=list()
        print()
        while(not self.is_empty()):
            value=self.delete()
            print(value,end="  ")
            lister.append(value)
        return lister
    def peek(self)->int:
        return self.heap_array[0]
    def print_heap(self):
        print()
        for i in range(self.size):
            print(self.heap_array[i],end="  ")

if __name__=='__main__':
    heap=Minheap(10)
    arr=[80,75,60,68,55,40,52,67]
    [heap.insert(value) for value in arr]
    heap.print_heap()
    heap.delete()
    heap.print_heap()
    result=heap.heap_sort()