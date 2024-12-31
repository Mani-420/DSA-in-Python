class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            return "Stack is empty"
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack items:", stack.display()) 
    print("Top item:", stack.peek())

    print("Popped item:", stack.pop()) 
    print("Stack items after pop:", stack.display()) 
    print("Is stack empty?", stack.is_empty())  
