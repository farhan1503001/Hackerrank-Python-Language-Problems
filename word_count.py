from collections import OrderedDict

if __name__=='__main__':
    num=int(input().strip())
    words=OrderedDict()
    for _ in range(num):
        key=input().strip()
        words[key]=words.get(key,0)+1
    print(len(words.keys()))
    for value in words.values():
        print(value,end=' ')
