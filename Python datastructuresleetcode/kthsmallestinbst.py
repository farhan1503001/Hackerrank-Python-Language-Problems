class TreeNode():
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
class solution():
    def __init__(self) -> None:
        self.answer=-2000000
    def insert_tree(self,root:TreeNode,value:int)->TreeNode:
        if root is None:
            return TreeNode(value)
        else:
            if(value<=root.value):
                root.left=self.insert_tree(root.left,value)
            else:
                root.right=self.insert_tree(root.right,value)
            return root
    def inorderk(self,root:TreeNode,)->None:
        if root is None:
            return
        self.inorderk(root.left)
        self.k-=1
        if self.k==0:
            self.answer=root.value
            return
        self.inorderk(root.right)
    def kthsmallest(self,root:TreeNode,k:int)->None:
        self.k=k
        self.inorderk(root)
        return self.answer

if __name__=='__main__':
    tree=TreeNode(5)
    sol=solution()
    sol.insert_tree(tree,3)
    sol.insert_tree(tree,2)
    sol.insert_tree(tree,4)
    sol.insert_tree(tree,7)
    sol.insert_tree(tree,6)
    print(sol.kthsmallest(tree,2))
    
    
        