import time
from collections import Counter
from typing import List
def countdown_timer():
    #Container list
    time_list=list()
    ###Here we will have our code
    ###Here our code ends timers start
    start=time.perf_counter()
    for i in range(10000000):
        time_list.append(i*2)
    end=time.perf_counter()
    return f'Code Runtime is {end-start:0.2f} seconds'
def counting_sequence(lister:List[int]):
    """
    This code finds how many times the sequence 1,5 occured
    """
    n=list(zip(lister[:-1],lister[1:]))
    print(n)
    n=Counter(n)[(1,5)]
    return n
if __name__=='__main__':
    print(countdown_timer())
    print(counting_sequence([2,1,5,4,3,1,5,8]))