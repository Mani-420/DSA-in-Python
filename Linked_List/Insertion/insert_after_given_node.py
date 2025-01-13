class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert a new node after a given node
def insertAfter(head, key, newData):
    curr = head
    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next
    # if curr becomes None means, given key is not found in linked list
    if curr is None:
        return head
    # Allocate new node by given data and point the next of newNode to curr's next & point current next to newNode
    newNode = Node(newData)
    newNode.next = curr.next
    curr.next = newNode
    return head


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    # Create the nodes
    head = Node(2)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(6)
    # Connecting the nodes
    head.next = node2
    node2.next = node3
    node3.next = node4

    key = 3
    newData = 4
    head = insertAfter(head, key, newData)
    printList(head)


if __name__ == "__main__":
    main()