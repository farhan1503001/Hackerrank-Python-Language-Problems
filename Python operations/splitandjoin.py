def split_and_join(value):
    res='-'
    value=value.split(' ')
    print(value)
    res=res.join(value)
    return res


if __name__=='__main__':
    string=input()
    res=split_and_join(string)
    print(res)