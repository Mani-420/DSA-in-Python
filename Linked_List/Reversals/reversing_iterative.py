class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Save the next node
        current.next = prev      # Reverse the link
        prev = current           # Move prev to current
        current = next_node      # Move current to the next node
    return prev  # New head of the reversed list

def display_nodes(head):
    current = head
    while current:
        print(current.data, end=" => ")
        current = current.next
    print("None")

# Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

# Connecting Nodes
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print("Original List:")
display_nodes(head)

head = reverse_list(head)

print("Reversed List:")
display_nodes(head)
