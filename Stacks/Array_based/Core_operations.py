class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.stack)
    print("Top item:", stack.peek())
    print("Stack size:", stack.size()) 
    print("Popped item:", stack.pop()) 
    print("Stack size:", stack.size()) 
    print("Is stack empty?", stack.is_empty())


if __name__ == "__main__":
    main()