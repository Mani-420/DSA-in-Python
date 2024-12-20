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

# Traversing in the linked list to print every number
head = node1
current = head
while current is not None:
    print(f"{current.data}")
    current = current.next
print("Every element has been printed.")