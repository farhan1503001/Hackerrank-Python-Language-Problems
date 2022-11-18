from typing import List
def remove_duplicates(lister:List[str])->List[str]:
    #better approach
    repeat_list=list()
    for value in lister:
        if value not in repeat_list:
            repeat_list.append(value)
        else:
            pass
    return repeat_list
#You can also use dictionary or set
def remove_duplicate_map(lister:List[str])->List[str]:
    map=set()
    for value in lister:
        map.add(value)
    print(map)
    return list(map)#set ekta korei valuerakhe repeat rakhe na eke list banaye send korlam
if __name__=='__main__':
    string_list=remove_duplicates(['be','be','be','is','not','not','not','not','or','question','that','the','to','to'])
    print(string_list)
    string_list=remove_duplicate_map(['be','be','be','is','not','not','not','not','or','question','that','the','to','to'])
    print(string_list)
    