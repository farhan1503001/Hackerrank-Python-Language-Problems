def swap_case(value):
    result=''
    result=result.join([val.lower() if val.isupper() else val.upper() for val in value])
    return result

if __name__=='__main__':
    stringinput=input()
    result=swap_case(stringinput)
    print(result)