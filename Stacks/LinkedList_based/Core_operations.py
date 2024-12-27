class Node:
    """A class representing a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """A class representing the stack using a linked list."""
    def __init__(self):
        self.top = None

    def push(self, data):
        """Add an item to the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove and return the top item of the stack."""
        if self.is_empty():
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            return "Stack is empty"
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements


# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack items:", stack.display())  # Output: [30, 20, 10]
    print("Top item:", stack.peek())  # Output: 30

    print("Popped item:", stack.pop())  # Output: 30
    print("Stack items after pop:", stack.display())  # Output: [20, 10]

    print("Is stack empty?", stack.is_empty())  # Output: False
