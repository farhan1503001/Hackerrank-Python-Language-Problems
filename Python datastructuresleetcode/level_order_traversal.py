class TreeNode():
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
def insert_alter(root:TreeNode,value:int)->TreeNode:
    if root is None:
       return TreeNode(value)
    else:
        if root.value>=value:
           root.left=insert_alter(root.left,value)
        else:
           root.right=insert_alter(root.right,value)
        return root
def level_order_traversal(root:TreeNode)->list:
    queue=list()
    answer=list()
    queue.append(root)
    while(len(queue)):
        length=len(queue)
        temp=[]
        for _ in range(length):
            q=queue.pop(0)
            temp.append(q.value)
            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)
        answer.append(temp)
    return answer
def pre_order_traversal(root:TreeNode)->None:
    if root is not None:
        print(root.value,end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
def in_order_traversal(root:TreeNode)->None:
    if root is not None:
        in_order_traversal(root.left)
        print(root.value,end=' ')
        in_order_traversal(root.right)
def post_order_traversal(root:TreeNode)->None:
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value,end=' ')
if __name__=='__main__':
    tree=TreeNode(5)
    insert_alter(tree,3)
    insert_alter(tree,2)
    insert_alter(tree,4)
    insert_alter(tree,7)
    insert_alter(tree,6)
    insert_alter(tree,8)
    lister=level_order_traversal(tree)
    print(lister)
    pre_order_traversal(tree)
    print()
    in_order_traversal(tree)
    print()
    post_order_traversal(tree)
