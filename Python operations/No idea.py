if __name__=='__main__':
    num,m=map(int,input().split())
    print(num,m)
    array=list(map(int,input().split()))
    #now inputting values for set-a
    set_a=set(map(int,input().split()))
    set_b=set(map(int,input().split()))
    #Now happiness counting
    counter=0
    for element in array:
        if element in set_a:
            counter+=1
        if element in set_b:
            counter-=1
    print(counter)