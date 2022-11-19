class node:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None

#First we have to know the height of a binary search tree
#Height mainly depends on right or left subtrees's height
#if left subtree height is greater than right subtree then we will take the left one and vice versa
def height_find(root):
    if root.left==None and root.right==None:
        return 0
    left=0
    if root.left!=None:
        left=height_find(root.left)
        
    right=0
    if root.right!=None:
        right=height_find(root.right)
        
        
    return max(left,right)+1
        
sum=[]

def calculate_level_sum(root,level):
    if root==None:
        return
    sum[level]+=root.key
    
    calculate_level_sum(root.left,level+1)
    calculate_level_sum(root.right,level+1)
    
    
    

# Create the binary tree
root = node(6)
root.left = node(4)
root.right = node(8)
root.left.left = node(3)
root.left.right = node(5)
root.right.left = node(7)
root.right.right = node(9)

height=height_find(root)+1

sum=[0]*height

calculate_level_sum(root,0)
print(sum)

        