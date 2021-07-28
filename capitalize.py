
if __name__=='__main__':
    input_string=input().split(' ')
    output=''
    print(input_string)
    for val in input_string:
        output+=val.capitalize()+' '
    print(output.rstrip())