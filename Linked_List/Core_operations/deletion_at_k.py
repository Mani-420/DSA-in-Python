# Creating Blue Prints for Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting Nodes
head.next = node2
node2.next = node3
node3.next = node4

# Deletion from the end
current = head 
while current.next.data != 30:
    current = current.next
current.next = current.next.next

# Printing the linked list
current = head
while current is not None:
    print(f"{current.data}")
    current = current.next