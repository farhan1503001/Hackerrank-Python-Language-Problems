class solution():
    def foursumcount(self,arr1:list,arr2:list,arr3:list,arr4:list)->int:
        memory=dict()
        for x in arr1:
            for y in arr2:
                target=x+y
                if target not in memory:
                    memory[target]=1
                else:
                    memory[target]+=1
        #find out opposite and add if u+v=-(u+v) previously exists add that to our count
        answer=0
        for u in arr3:
            for v in arr4:
                target=-(u+v)
                #check opposition exists or not
                if target in memory:
                    answer+=memory[target]
        return answer

if __name__=='__main__':
    arr1=[-1,1]
    arr2=[1,-1]
    arr3=[-2,2]
    arr4=[2,-2]
    print(solution().foursumcount(arr1,arr2,arr3,arr4))
