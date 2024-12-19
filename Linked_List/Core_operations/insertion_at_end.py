# Creating Blue Prints for Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting Nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Adding New Node at the Start
head = node1
new_node = Node(50)
current = head

while current.next is not None:
    current = current.next
current.next = new_node

# Printing the linked list 
current = node1
while current is not None:
    print(f"{current.data}")
    current = current.next