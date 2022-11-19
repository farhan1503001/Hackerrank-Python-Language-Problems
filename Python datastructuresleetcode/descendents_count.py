
class Node:
    def __init__(self,key) -> None:
        self.left=None
        self.right=None
        self.val=key
        
def count_nodes(root):
    if root == None:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)   
def inorder(root):
    if root:
        val=count_nodes(root)
        print(root.val)
        print("Subtree node number is: ",val-1)
        inorder(root.left)
        inorder(root.right)
    
    

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("\nInorder traversal of binary tree is")
inorder(root)