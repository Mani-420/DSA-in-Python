# Creating Blue Prints for Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Searching function 
def searching(head, target):
    current = head
    node_number = 1

    while current:
        if current.data == target:
            return f"The searched value '{target}' is at node number: {node_number}"
        current = current.next
        node_number += 1
    
    return f"The {target} is not in linked list."

# Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connecting Nodes
head.next = node2
node2.next = node3
node3.next = node4

user_input = int(input("Enter the value to search: "))
result = searching(head, user_input)
print(result)