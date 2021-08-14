from typing import List


class solution():
    def group_anagrams(self,strings:List[str])->List[List[str]]:
        hashmap=dict([])
        for word in strings:
            sorted_word=''.join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word]=[]
            hashmap[sorted_word].append(word)
        
        answer=[]
        for word in hashmap.values():
            #print(word)
            answer.append(word)
        return answer

if __name__=='__main__':
    words=list(map(str,input().split()))
    #print(words)
    '''''
    word1=''.join(sorted(words[0]))
    print(word1)
    '''''
    sol=solution()
    angram_group=sol.group_anagrams(words)
    print([value for value in angram_group])