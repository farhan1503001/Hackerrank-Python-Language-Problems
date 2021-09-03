
class solution():
    def lengthofLongestString(self,s:str)->int:
        char_dict=dict()
        start=0
        maxlen=0
        for index,char in enumerate(s):
            #we opt not to consider recurrent char
            if char in char_dict:
                start=max(start,char_dict[char]+1)
            maxlen=max(maxlen,index-start+1)#finding length
            char_dict[char]=index #setting char in dict
        return maxlen

if __name__=='__main__':
    print(solution().lengthofLongestString('abcabcbb'))
        