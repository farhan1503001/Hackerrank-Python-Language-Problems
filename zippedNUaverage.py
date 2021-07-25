
if __name__=='__main__':
    num_subject,num_student=map(int,input().split())
    marks=list()
    for _ in range(num_student):
        marks.append(list(map(float,input().split())))

    [print(sum(mark)/len(mark)) for mark in zip(*marks)]
