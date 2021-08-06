def counter(func):
    def wrapper(*args,**kwargs):
        wrapper.count+=1
        func(*args,**kwargs)
    wrapper.count=0
    return wrapper
def run_n_times(n):
    """Define and Return a decorator"""
    def decorator(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator
@counter
def foot_print():
    print("Calling foot_print()")
@run_n_times(10)
def multiply(a,b):
    print(a*b)
if __name__=='__main__':
     foot_print()
     foot_print()
     foot_print()
     print('foot_print() function was called {} times'.format(foot_print.count))
     #run_n_times(10)(multiply(30,20))
     multiply(30,30)