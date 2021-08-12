class TreeNode():
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
class solution():
    def hassum(self,root:TreeNode,targetsum:int,current_value:int)->bool:
        if root is None:
            return False
        current_value+=root.value
        if current_value==targetsum and (root.left is None and root.right is None):
            return True
        return self.hassum(root.left,targetsum,current_value) or self.hassum(root.right,targetsum,current_value)
        
    def hasPathSum(self,root:TreeNode,targetsum:int)->bool:
        return self.hassum(root,targetsum,0)
    def insert_tree(self,root:TreeNode,value:int)->TreeNode:
        if root is None:
            return TreeNode(value)
        else:
            if(value<=root.value):
                root.left=self.insert_tree(root.left,value)
            else:
                root.right=self.insert_tree(root.right,value)
            return root
        

if __name__=='__main__':
    tree=TreeNode(5)
    sol=solution()
    sol.insert_tree(tree,3)
    sol.insert_tree(tree,2)
    sol.insert_tree(tree,4)
    sol.insert_tree(tree,7)
    sol.insert_tree(tree,6)
    print(sol.hasPathSum(tree,15))
    