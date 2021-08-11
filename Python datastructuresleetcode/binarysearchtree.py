
class binary_search_tree:
    def __init__(self,value:int) -> None:
        self.value=value
        self.left=None
        self.right=None
    
def insert(root:binary_search_tree,value:int)->None:
    if root is None:
        root=binary_search_tree(value)
        return
    else:
        if root.value>=value:
            if root.left is None:
                root.left=binary_search_tree(value)
            else:
                insert(root.left,value)
        else:
            if root.right is None:
               root.right=binary_search_tree(value)
            else:
                insert(root.right,value)
def insert_alter(root:binary_search_tree,value:int)->binary_search_tree:
    if root is None:
       return binary_search_tree(value)
    else:
        if root.value>=value:
           root.left=insert_alter(root.left,value)
        else:
           root.right=insert_alter(root.right,value)
        return root
def minimum_value(root:binary_search_tree)->binary_search_tree:
    curr=root
    while(curr.left is not None):
        curr=curr.left
    return curr
def delete(root:binary_search_tree,value:int)->binary_search_tree:
    if root is None:
        return root
    else:
        if root.value>value:
            root.left=delete(root.left,value)
        elif root.value<value:
            root.right=delete(root.right,value)
        else:
            #Match found look for one child
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=minimum_value(root.right) #Find smallest element in right subtree
            root.value=temp.value
            root.right=delete(root.right,temp.value)
        return root
def preorder_traverse(root:binary_search_tree)->None:
    if root is not None:
        print(root.value,end=' ')
        preorder_traverse(root.left)
        preorder_traverse(root.right)
def search(root:binary_search_tree,key:int)->None:
    if root is None:
        print(str(key)+" is not found")
        return
    if root.value==key:
        print(str(key)+" is found")
        return
    elif root.value>key:
        search(root.left,key)
    else:
        search(root.right,key)


if __name__=='__main__':
    tree=binary_search_tree(5)
    insert(tree,3)
    insert(tree,2)
    insert(tree,4)
    insert(tree,7)
    insert(tree,6)
    insert(tree,8)
    preorder_traverse(tree)
    tree1=binary_search_tree(5)
    insert_alter(tree1,3)
    insert_alter(tree1,2)
    insert_alter(tree1,4)
    insert_alter(tree1,7)
    insert_alter(tree1,6)
    insert_alter(tree1,8)
    print()
    preorder_traverse(tree1)
    print()
    search(tree1,8)
    delete(tree1,7)
    print()
    preorder_traverse(tree1)

    

