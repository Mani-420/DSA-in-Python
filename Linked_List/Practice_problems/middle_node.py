# Creating Blue Prints for Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

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
result = middleNode(head)
print(f"The middle part of linked List is: {result.data}") 

