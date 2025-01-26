# A node structure
class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None


def printLevelOrder(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        print (queue[0].data, end= " ")
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

# Driver Program to test above function
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print ("Level Order Traversal of binary tree is -")
    printLevelOrder(root)  

if __name__ == "__main__":
    main()
