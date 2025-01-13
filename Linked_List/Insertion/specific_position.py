class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_position(head, position, data):
    new_node = Node(data)
    # If inserting at the beginning
    if position == 1:
        new_node.next = head
        head = new_node
        return head

    current = head
    for _ in range(1, position - 1):
        if current is None:
            break
        current = current.next
    # If the position is out of bounds
    if current is None:
        print("Position is out of bounds.")
        return head

    new_node.next = current.next
    current.next = new_node
    return head


def print_list(head):
    while head:
        print(f" {head.data}", end="")
        head = head.next
    print()


def main():
    # Create the nodes
    head = Node(3)
    node2 = Node(5)
    node3 = Node(8)
    node4 = Node(10)
    # Connecting the nodes
    head.next = node2
    node2.next = node3
    node3.next = node4
    
    data, pos = 12, 2
    head = insert_at_position(head, pos, data)
    print_list(head)
    
    
if __name__ == "__main__":
    main()