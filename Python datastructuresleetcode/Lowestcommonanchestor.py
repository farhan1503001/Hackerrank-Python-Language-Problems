class TreeNode():
    def __init__(self,value) -> None:
        self.data=value
        self.left=None
        self.right=None
class Solution():
    def insert_tree(self,root:TreeNode,value:int)->TreeNode:
        if root is None:
            return TreeNode(value)
        else:
            if value<=root.data:
                root.left=self.insert_tree(root.left,value)
            else:
                root.right=self.insert_tree(root.right,value)
            return root
    def lowest_common_anchestor(self,root:TreeNode,n1:int,n2:int)->TreeNode:
        if root is None:
            return
        if root.data==n1 or root.data==n2:
            return root
        left=self.lowest_common_anchestor(root.left,n1,n2) #Both left and right has match
        right=self.lowest_common_anchestor(root.right,n1,n2)

        if left is not None and right is not None:
            return root #Lowest anchestor as it has both left and right child which matches our value
        if left is None and  right is None:
            return None #No match has been found
        if left is None:
            return right
        if right is None:
            return left
    def inorder(self,root:TreeNode)->None:
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
if __name__=='__main__':
    tree=TreeNode(5)
    sol=Solution()
    sol.insert_tree(tree,3)
    sol.insert_tree(tree,2)
    sol.insert_tree(tree,4)
    sol.insert_tree(tree,7)
    sol.insert_tree(tree,6)
    result=sol.lowest_common_anchestor(tree,3,4)
    print('LCA is : ',result.data)


            
        