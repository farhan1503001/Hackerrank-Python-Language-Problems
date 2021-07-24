def fibonacci(n):
    fibonacci_array=list()
    f1=0
    f2=1
    if n>0:
        fibonacci_array.append(f1)
        for i in range(n-1):
            sum=f1+f2
            f1=f2
            f2=sum
            fibonacci_array.append(f1)
            #print(f1)
    else:
        pass
    return fibonacci_array
    
cube=lambda x: x*x*x
if __name__=='__main__':
    n=int(input().strip())
    pr_list=list(map(cube,fibonacci(n)))
    print(pr_list)
