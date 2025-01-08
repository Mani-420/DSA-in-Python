class Node:
    # Constructor of a Node.
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    # Constructor of a deque.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):                     # To check if it is empty.
        return self.size == 0

    def append(self, value):                # Add element to the right side.
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendleft(self, value):            # Add element to the left side.
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):                          # Remove and return an element from the right side.
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def popleft(self):                      # Remove and return an element from the left side.
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def peek_left(self):                    # To view the leftmost element.
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.head.value

    def peek_right(self):                   # To view the leftmost element.
        if self.is_empty():
            raise IndexError("peek from an empty deque")
        return self.tail.value

    def __len__(self):
        return self.size

# Example usage
dq = Deque()

# Add elements
dq.append(10)
dq.appendleft(20)
dq.append(30)
print("Deque after additions:", [dq.peek_left(), dq.peek_right()])

# Remove elements
print("Popped right:", dq.pop())
print("Popped left:", dq.popleft())
print("Deque size after removals:", len(dq))
