class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list_recursive(current, prev=None):
    if not current:  # Base case: End of the list
        return prev  # New head of the reversed list
    next_node = current.next  # Save the next node
    current.next = prev      # Reverse the link
    return reverse_list_recursive(next_node, current)  # Recur with next node and current as prev

def display_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example Usage
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4

print("Original List:")
display_list(node1)

# Reversing the list recursively
reversed_head = reverse_list_recursive(node1)

print("Reversed List:")
display_list(reversed_head)
