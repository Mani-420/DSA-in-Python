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
node5 = Node(50)

# Connecting Nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Creating a new node at k
new_node = Node(60)

#Insertion the New Node at k
current = node1
while current is not None and current.data != 30:
    current = current.next
new_node.next = current.next        #Attaching new node at the specific position
current.next = new_node    

# Printing the linked list 
current = node1
while current is not None:
    print(f"{current.data}")
    current = current.next