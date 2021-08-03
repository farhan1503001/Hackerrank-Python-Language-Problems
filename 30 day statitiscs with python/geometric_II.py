if __name__=='__main__':
    nm,dm=map(int,input().split())
    num_of_event=int(input().strip())
    probs=nm/dm
    result=sum([probs*((1-probs)**(event-1)) for event in range(1,num_of_event+1)])
    print(round(result,3))
