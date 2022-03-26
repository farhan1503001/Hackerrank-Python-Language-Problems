
from typing import List

def stutter(nums:List[int])->list[int]:
    nums=[value for value in nums for i in range(2)]
    print(nums)
    #deactivate upper lines while submitting just active return line
    return [value for value in nums for i in range(2)]

def remove_duplicates(lister:List[str])->List[str]:
    #Naive approach
    repeat_list=list()
    for value in lister:
        if value not in repeat_list:
            repeat_list.append(value)
        else:
            pass
    return repeat_list
   #You can also use dictionary or set
if __name__=='__main__':
    nums=stutter([1,2,3])
    print(nums)
    string_list=remove_duplicates(['be','be','be','is','not','not','not','not','or','question','that','the','to','to'])
    print(string_list)
    