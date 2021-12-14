from typing import List
class solution():
    def find_repeated_sequences(s:str)->List[str]:
        #hashmap creation
        sequence_store=dict()
        repeat_list=[]
        for i in range(0,len(s)-10):
            sub_str=s[i:i+10]
            if sub_str not in sequence_store:
                sequence_store[sub_str]=1
            else:
                sequence_store[sub_str]=sequence_store[sub_str]+1
        
        for word in sequence_store.keys():
            if sequence_store[word]>1:
                repeat_list.append(word)
            else:
                pass
        return repeat_list

if __name__=='__main__':
    result=solution.find_repeated_sequences("AAAAAAAAAAAAA")
    print(result)
