# Python Program to Insert a Node at the End of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function appends a new node at the end and returns the head.
def insertAtEnd(head, new_data):
    # Create a new node
    new_node = Node(new_data)
    # If the Linked List is empty, make the
    # new node as the head and return
    if head is None:
        return new_node

    # Store the head reference in a temporary variable
    last = head
    # Traverse till the last node
    while last.next:
        last = last.next

    # Change the next pointer of the last node to point to the new node
    last.next = new_node
    # Return the head of the list
    return head


def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next


def main():
    # Create the nodes
    head = Node(2)
    node2 = Node(3)
    node3 = Node(4)
    node4 = Node(5)
    node5 = Node(6)
    # Connecting the nodes
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    head = insertAtEnd(head, 1)
    print_list(head)


if __name__ == "__main__":
    main()