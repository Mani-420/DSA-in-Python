'''
-> Preorder (Root, Left, Right)

-> Algorithm Preorder(tree):
    -> Visit the root.
    -> Traverse the left subtree, i.e., call Preorder(left-subtree)
    -> Traverse the right subtree, i.e., call Preorder(right-subtree)
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.value),
        # Then recur on left child
        printPreorder(root.left)
        # Finally recur on right child
        printPreorder(root.right)


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
    printPreorder(root)


if __name__ == "__main__":
    main()