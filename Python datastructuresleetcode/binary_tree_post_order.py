
from typing import List
class TreeNode:
    def __init__(self,value) -> None:
        self.data=value
        self.left=None
        self.right=None
class solution():
    def post_order_traversal(self,root:TreeNode)->List[int]:
        stack1=[]
        stack2=[]
        stack1.append(root)
        ans=list()
        while(len(stack1)):
            u=stack1.pop()
            stack2.append(u)
            if (u.left):
                stack1.append(u.left)
            if (u.right):
                stack1.append(u.right)
        while(len(stack2)):
            result=stack2.pop()
            print(result.data,end=" ")
            ans.append(result.data)
        return ans

if __name__=='__main__':
    root = TreeNode(4)
    root.left = TreeNode(5)
    root.right = TreeNode(6)
    root.left.left = TreeNode(7)
    root.right.right=TreeNode(8)
    root.right.left=TreeNode(10)
    sol=solution()
    result=sol.post_order_traversal(root)
    print([value for value in result])

