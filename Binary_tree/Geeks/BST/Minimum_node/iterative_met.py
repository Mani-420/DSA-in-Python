# Python code to find minimum value in BST using using iterationl
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minValue(root):
    # base case
    if root is None:
        return -1
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr.data

def main():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.left.left = Node(3)
    root.right.right = Node(7)
    root.left.left.left = Node(1)

    print(minValue(root))

if __name__ == "__main__":
    main()