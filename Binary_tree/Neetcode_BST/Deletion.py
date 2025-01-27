class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def del_node(root, x):
    if not root:
        return None
    
    if root.key < x:
        root.right = del_node(root.right, x)
    elif root.key > x:
        root.left = del_node(root.left, x)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.key = minNode.key
            root.right = del_node(root.right, minNode.key)
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