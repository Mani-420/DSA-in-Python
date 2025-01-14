class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def search_key(head, key):
    # Initialize curr with the head of linked list
    curr = head
    # Iterate over all the nodes
    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next
    # If there is no node with value as key, return false
    return False


def main():
    # Example Usage
    head = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    # Linking the nodes
    head.next = node2
    node2.next = node3
    node3.next = node4

    # Key to search in the linked list
    key = 40
    if search_key(head, key):
        print("The search value is present in LinkedList")
    else:
        print("The search value is not present in LinkedList")


if __name__ == "__main__":
    main ()