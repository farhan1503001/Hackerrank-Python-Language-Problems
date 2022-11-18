if __name__=='__main__':
    input_file=input("Input file?")
    with open(input_file) as filer:
        for line in filer:
            temp_list=line.split(' ')
            #print(temp_list)
            Id=temp_list[0]
            name=temp_list[1]
            total=0.0
            avg=0.0
            days=0
            for i in range(2,len(temp_list)):
                total=total+float(temp_list[i])
                days+=1
            avg=total/days
            print(name+" "+"(ID#"+Id+") worked "+str(total)+" ("+str(avg)+"/day)")