# Python code to find minimum value in BST using recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def minValue(root):
    if root is None or root.left is None:
        return root.data
    return minValue(root.left)

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