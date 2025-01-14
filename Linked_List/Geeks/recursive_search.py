class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


def searchKey(head, key):
    # Base case
    if head is None:
        return False

    # If key is present in current node, return true
    if head.data == key:
        return True
    # Recur for remaining list
    return searchKey(head.next, key)


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
    key = 10
    if searchKey(head, key):
        print("The search value is present in LinkedList")
    else:
        print("The search value is not present in LinkedList")


if __name__ == "__main__":
    main()