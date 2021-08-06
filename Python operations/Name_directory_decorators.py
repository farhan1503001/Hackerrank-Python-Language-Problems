def name_directory_decorator(func):
    def wrapper(*args):
        sorted_array=sorted(*args,key=lambda x: int(x[2]))
        for item in sorted_array:
            yield func(item)
    return wrapper
@name_directory_decorator
def name_format(person):
    """adds appropriate salutation to sorted people's name
    Args:
        list containing people's name
    """
    return ("Mr. " if person[3]=='M' else "Ms. ")+str(person[0])+" "+str(person[1])
if __name__=='__main__':
    people=[input().split() for _ in range(int(input().strip()))]
    print(people)
    print(*name_format(people),sep='\n')