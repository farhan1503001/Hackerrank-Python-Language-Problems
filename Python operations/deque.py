from collections import deque
if __name__=='__main__':
    test_case=int(input().strip())
    queue=deque()
    while(test_case):
        commands=input().split()
        #print(command)
        command=commands[0]
        if len(commands)>1:
             value=int(commands[1])
        if command=='append':
            queue.append(value)
        elif command=='appendleft':
            queue.appendleft(value)
        elif command=='pop':
            queue.pop()
        elif command=='popleft':
            queue.popleft()
        else:
            pass
        test_case-=1
    
    for val in queue:
        print(val,end=' ')

        
        

