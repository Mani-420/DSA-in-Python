''' 
-> Inorder (Left, Root, Right)

-> Algorithm Inorder(tree):
    -> Traverse the left subtree, i.e., call Inorder(left-subtree)
    -> Visit the root.
    -> Traverse the right subtree, i.e., call Inorder(right-subtree)

'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.value)
        # now recur on right child
        printInorder(root.right)


# Driver code
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("\nInorder traversal of binary tree is: ")
    printInorder(root)


if __name__ == "__main__":
    main()