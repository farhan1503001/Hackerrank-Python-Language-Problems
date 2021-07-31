from collections import namedtuple
if __name__=='__main__':
    num=int(input().strip())
    columns=input().split()
    student=namedtuple('student',columns)
    marks=0
    for i in range(num):
        fields=list(input().split())
        students=student(fields[0],fields[1],fields[2],fields[3])
        marks+=int(students.MARKS)
    print('{:.2f}'.format(marks/num))

        