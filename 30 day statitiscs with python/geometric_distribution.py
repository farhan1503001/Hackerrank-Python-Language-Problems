if __name__=='__main__':
    nm,dm=map(int,input().split())
    num_of_events_after=int(input().strip())
    probs=nm/dm
    probablity=probs*((1-probs)**(num_of_events_after-1))
    print(round(probablity,3))