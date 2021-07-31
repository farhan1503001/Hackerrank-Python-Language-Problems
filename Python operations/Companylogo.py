from collections import Counter

if __name__=='__main__':
    input_string=input().strip()
    counter=Counter(input_string)
    print(counter)
    sorted_counter=sorted(counter.items(),key=lambda x:(-x[1],x[0]))
    print(sorted_counter)
    count=0
    for value in sorted_counter:
        if(count==3):
            break
        print(value[0],value[1])
        count+=1