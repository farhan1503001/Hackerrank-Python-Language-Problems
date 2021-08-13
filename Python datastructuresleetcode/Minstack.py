class MinStack():
    def __init__(self) -> None:
        self.stack=list()
    def get_min(self):
        return self.stack[-1][1] if self.stack else None
    def push(self,value:int)->None:
        current_min=self.get_min()
        if current_min is None or current_min>value:
            current_min=value
        self.stack.append((value,current_min))
    def pop(self)->None:
        self.stack.pop()
    def top(self)->int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

if __name__=='__main__':
    stack=MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(33)
    stack.push(-22)
    print(stack.get_min())
    print(stack.top())
    stack.pop()
    print(stack.get_min())
    print(stack.top())
    
