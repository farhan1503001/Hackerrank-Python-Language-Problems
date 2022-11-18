def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
        
    return fact
def maximum_finder(lister):
    max=lister[0]
    for i in range(1,len(lister)):
        if max<lister[i]:
            max=lister[i]
            
    print("Maximum number is: ",max)
    return max

