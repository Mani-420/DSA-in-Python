class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def del_node(root, x):
    # Base case
    if root is None:
        return root
    # If key to be searched is in a subtree
    if root.key > x:
        root.left = del_node(root.left, x)
    elif root.key < x:
        root.right = del_node(root.right, x)
    else:
        # Cases when root has 0 children or only right child
        if root.left is None:
            return root.right
        # When root has only left child
        if root.right is None:
            return root.left
        # When both children are present
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)
        
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    x = 15

    root = del_node(root, x)
    inorder(root)
    print()
    
if __name__ == "__main__":
    main()