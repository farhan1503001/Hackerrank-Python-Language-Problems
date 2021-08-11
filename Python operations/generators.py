def fibonacci(n):
    f1=0
    f2=1
    for _ in range(1,n):
        yield f2
        temp=f2
        f2=f1+f2
        f1=temp

def get_lengths(lister):
    for value in lister:
        yield value,len(value)

if __name__=='__main__':
    """Creating a generator using()
    """
    number_gen=(item for item in range(100) if item%3==0 and item%7==0)
    print(number_gen)
    print(next(number_gen))
    print(next(number_gen))
    lannisters=['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
    length_lan=((member,len(member)) for member in lannisters)
    print(next(length_lan))
    for person in length_lan:
        print(person)
    fib_find=fibonacci(10)
    print(next(fib_find))
    print(next(fib_find))
    print(next(fib_find))
    print(next(fib_find))
    iterator=get_lengths(lannisters)
    print(next(iterator))
    print(next(iterator))