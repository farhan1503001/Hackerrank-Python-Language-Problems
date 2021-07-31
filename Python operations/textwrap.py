import textwrap

def wrap(string,width):
    return '\n'.join([string[i:i+width] for i in range(0,len(string),width)])

if __name__=='__main__':
    s=input().strip()
    num=int(input().strip())
    for i in range(0,len(s)-num,num):
        print(s[i:i+num])

    print(s[i+num:])
    print(wrap(s,num))