'''
-> Postorder (Left, Right, Root)

-> Algorithm Postorder(tree):
    -> Traverse the left subtree, i.e., call Postorder(left-subtree).
    -> Traverse the right subtree, i.e., call Postorder(right-subtree).
    -> Visit the root.
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # the recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.value),


# Driver code
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("\nPostorder traversal of binary tree is: ")
    printPostorder(root)


if __name__ == "__main__":
    main()
