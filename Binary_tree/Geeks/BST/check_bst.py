# Python program to check if a tree is BST using Inorder Traversal
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Recursive Function for inorder traversal
def inorder(root, prev):
    if root is None:
        return True
    # Recursively check the left subtree
    if not inorder(root.left, prev):
        return False
    # Check the current node value against the previous value
    if prev[0] >= root.data:
        return False
    # Update the previous value to the current node's value
    prev[0] = root.data
    # Recursively check the right subtree
    return inorder(root.right, prev)

# Function to check if the tree is a valid BST
def isBST(root):
    prev = [float('-inf')]
    return inorder(root, prev)

def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if isBST(root):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()