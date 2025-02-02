# Python Program to convert binary tree to binary search tree.
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Inorder traversal to store the nodes in a vector
def inorder(root, nodes):
    if root is None:
        return
    inorder(root.left, nodes)
    nodes.append(root.data)
    inorder(root.right, nodes)

# Inorder traversal to convert tree to BST.
def constructBst(root, nodes, index):
    if root is None:
        return
    constructBst(root.left, nodes, index)
    # Update root value
    root.data = nodes[index[0]]
    index[0] += 1
    constructBst(root.right, nodes, index)

# Function to convert a binary tree to a binary search tree
def binaryTreeToBst(root):
    nodes = []
    inorder(root, nodes)
    # sort the nodes
    nodes.sort()
    index = [0]
    constructBst(root, nodes, index)
    return root

# Function to print the inorder traversal of a binary tree
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

def main():
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(4)

    ans = binaryTreeToBst(root)
    printInorder(ans)

if __name__ == "__main__":
    main()