
from typing import List


class solution():
    def avgSalary(self,salary:List[int])->float:
        max_salary=max(salary)
        min_salary=min(salary)
        return sum([val for val in salary if val!=max_salary and val!=min_salary ])/(len(salary)-2)
if __name__=='__main__':
    print(solution().avgSalary([4000,3000,1000,2000]))