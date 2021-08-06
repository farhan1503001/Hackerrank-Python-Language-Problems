def phone_num_decorator(func):
    def wrapper(lister):
        func(["+91 "+item[-10:-5]+" "+item[-5:] for item in lister])
    return wrapper

@phone_num_decorator
def sort_phone(lister):
    """prints the phone numbers in desired sorted order
    Args:
       lister: a list of phone numbers
    """
    print(*sorted(lister),sep='\n')
if __name__=='__main__':
    arr=[input() for i in range(int(input().strip()))]
    #print(arr[0][-10])
    sort_phone(arr)
    