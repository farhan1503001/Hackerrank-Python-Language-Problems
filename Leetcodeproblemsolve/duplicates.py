class solution():
    def duplicate_finder(self,arr:list)->tuple:
        map={}
        for value in arr:
            if value not in map:
                map[value]=1
            if value in map:
                map[value]+=1
                return (value,True)

if __name__=='__main__':
    arr=[1,2,4,5,1]
    print(solution().duplicate_finder(arr))