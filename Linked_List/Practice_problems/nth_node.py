# Creating Blue Prints for Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def nth_node_end(head, n):
    first = head
    second = head
    
    for _ in range(n):
        if not first:
            return None
        first = first.next

    while first:
        first = first.next
        second = second.next
    return second

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

# Calling the function
n = 4
result = nth_node_end(head, n)
print(f"The nth node of linked List is: {result.data}") 