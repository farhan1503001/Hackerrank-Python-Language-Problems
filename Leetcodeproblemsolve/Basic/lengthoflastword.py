
class solution():
    def lengthofLastWord(self,s:str)->int:
        return len(s.rstrip().split()[-1]),s.rstrip().split()[-1]

if __name__=='__main__':
    print(solution().lengthofLastWord("luffy is still joyboy"))
    print(solution().lengthofLastWord("   fly me   to   the moon  "))
