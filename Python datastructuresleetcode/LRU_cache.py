from collections import deque
class LRUcache():
    def __init__(self,size:int) -> None:
        self.queue=deque()
        self.memory=dict()
        self.size=size
    def put(self,key:int,value:int)->None:
        if key not in self.memory:
            if len(self.queue)==self.size:
                least_used_val=self.queue.popleft()
                #remove value also from memory
                del self.memory[least_used_val]
        else: #if the key exists in queue just remove the shit out of it
            self.queue.remove(key)
        #Now perform append operation 
        self.queue.append(key)
        self.memory[key]=value
    def get(self,key:int)->int:
        if key not in self.memory:
            return -1
        else:
            value=self.memory[key]
            #Remove the key and sent it to first position
            self.queue.remove(key)
            self.queue.append(key)
    def queue_print(self)->None:
       print([val for val in self.queue])

if __name__=='__main__':
    lr=LRUcache(5)
    lr.put(1,1000)
    lr.put(2,2000)
    lr.put(3,3000)
    lr.queue_print()
    lr.get(3)
    lr.queue_print()
