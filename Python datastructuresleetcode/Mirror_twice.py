from typing import List
def has_mirror_twice(a1:List[int],a2:List[int])->bool:
    len_a1=len(a1)
    len_a2=len(a2)
    count=0
    if len_a2>len_a1:
        return False
    else:
        limit=len_a1-len_a2+1
        #just first string er sei porjonto iterate hobe jekhane theke a-2 er soman length pabo
        for index in range(limit):
            sub_string_index=0
            while(sub_string_index<len_a2):
                if a1[index+sub_string_index]!=a2[-sub_string_index-1]:
                    #jodi na mele break,ultamelanorjonno minus
                    break
                sub_string_index+=1
            if sub_string_index==len_a2:
                #Jodi milejai then break count korte hobe
                count=count+1
        print(count)      
        if count>=2:
            return True
        else:
            return False
    
if __name__=='__main__':
    print(has_mirror_twice([6,1,2,1,3,1,3,2,1,5],[1,2]))
    print(has_mirror_twice([5,8,4,18,5,42,4,8,5,5],[4,8,5]))