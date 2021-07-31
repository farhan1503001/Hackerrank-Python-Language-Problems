def substring_finder(value1,value2):
    len_str1=len(value1)
    len_str2=len(value2)
    count=0
    for i in range(len_str1-len_str2+1):
        #print(value1[i:])
        if value1[i:].startswith(str2):
            count+=1
    print(count)




if __name__=='__main__':
    str1=input().strip()
    str2=input().strip()
    num=substring_finder(str1,str2)