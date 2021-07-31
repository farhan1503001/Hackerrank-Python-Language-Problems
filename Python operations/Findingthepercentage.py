
if __name__=='__main__':
    num=int(input().strip())
    marks=dict()
    for _ in range(num):
        line=input().split()
        marks[line[0]]=list(map(float,line[1:]))
        #print(marks[line[0]])
    query=input().strip()
    print('{0:.2f}'.format(sum(marks[query])/len(marks[query])))