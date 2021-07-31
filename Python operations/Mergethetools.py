
if __name__=='__main__':
    string1=input().strip()
    k=int(input().strip())
    store=[string1[i:i+k] for i in range(0,len(string1),k)]
    for value in store:
        dictionary=dict()
        printer=''
        for i in range(len(value)):
            if dictionary.get(value[i]) is None:
                printer=printer+value[i]
                dictionary[value[i]]=True
            else:
                pass
        print(printer)
