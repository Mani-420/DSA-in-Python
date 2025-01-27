class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# function to search a key in a BST
def search(root, key):
    if root is None or root.key == key:
        return root
    
    if root.key < key:
        return search(root.right, key)
    
    return search(root.left, key)

def main():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    # Searching for keys in the BST
    print("Found" if search(root, 19) else "Not Found")
    print("Found" if search(root, 80) else "Not Found")
    
if __name__ == "__main__":
    main()
