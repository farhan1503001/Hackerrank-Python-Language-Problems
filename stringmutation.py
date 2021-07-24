def mutation_1(value,i,k):
    res=value[:i]+str(k)+value[i+1:]
    return res
def mutation_2(value,i,k):
    res=list(value)
    res[i]=k
    stringman=''.join(res)
    print(stringman)

if __name__=='__main__':
    string=input()
    position,char=input().split()
    res=mutation_1(string,int(position),char)
    print(res)
    mutation_2(string,int(position),char)