from collections import deque

# A node structure
class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None


def bfs(root):
    queue = deque()
    if root:
        queue.append(root)

    level = 0
    while(len(queue) > 0):
        print (f"Level: {level}")
        for i in range(len(queue)):
            current = queue.popleft()
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        level += 1

# Driver Program to test above function
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print ("Level Order Traversal of binary tree is: ")
    bfs(root)  

if __name__ == "__main__":
    main()
