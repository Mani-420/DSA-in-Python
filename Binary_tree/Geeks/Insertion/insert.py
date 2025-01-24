# Python program to insert element (in level order) in Binary Tree
from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def InsertNode(root, data):
    if root is None:
        root = Node(data)
        return root

    q = deque()
    q.append(root)

    while q:
        curr = q.popleft()
        if curr.left is not None:
            q.append(curr.left)
        else:
            curr.left = Node(data)
            return root

        if curr.right is not None:
            q.append(curr.right)
        else:
            curr.right = Node(data)
            return root

# Inorder traversal of a binary tree
def inorder(curr):
    if curr is None:
        return
    inorder(curr.left)
    print(curr.data, end=' ')
    inorder(curr.right)

def main():
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)

    key = 12
    root = InsertNode(root, key)

    inorder(root)

if __name__ == "__main__":
    main()