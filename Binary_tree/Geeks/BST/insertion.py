class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def printLevelOrder(root):
    if root is None:
        return

    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print (queue[0].val, end= " ")
        node = queue.pop(0)
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver program to test the above functions
def main():
    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    # Print level order traversal of the BST
    printLevelOrder(root)
    
if __name__ == "__main__":
    main()
