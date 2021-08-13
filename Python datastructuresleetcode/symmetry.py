class TreeNode():
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
class solution():
    def insert(self,root:TreeNode,value:int)->TreeNode:
        if root is None:
            return TreeNode(value)
        else:
            if value<=root.data:
                root.left=self.insert(root.left,value)
            else:
                root.right=self.insert(root.right,value)
            return root 
    def is_mirror(self,node_1:TreeNode,node_2:TreeNode):
        if node_1 is None and node_2 is None:
            return True
        if node_1 is not None or node_2 is not None:
            return False
        return (node_1.data==node_2.data) and self.is_mirror(node_1.left,node_2.right) and self.is_mirror(node_1.right,node_2.left)
    def is_symmetric(self,root:TreeNode):
        return self.is_mirror(root,root)


if __name__=='__main__':
    tree=TreeNode(5)
    sol=solution()
    sol.insert(tree,3)
    sol.insert(tree,2)
    sol.insert(tree,4)
    sol.insert(tree,7)
    sol.insert(tree,6)
    print(sol.is_symmetric(tree))