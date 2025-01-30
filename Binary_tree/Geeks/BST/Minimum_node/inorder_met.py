# Python code to find minimum value in BST using inorder traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root, sorted_inorder):
    # Base Case
    if root is None:
        return
    inorder(root.left, sorted_inorder)
    sorted_inorder.append(root.data)
    inorder(root.right, sorted_inorder)

def minValue(root):
    if root is None:
        return -1
    sorted_inorder = []  
    inorder(root, sorted_inorder)
    # Return the first element, which is the minimum
    return sorted_inorder[0]

# Driver program to test the above functions
def main():
    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 10)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print(minValue(root))

if __name__ == "__main__":
    main()