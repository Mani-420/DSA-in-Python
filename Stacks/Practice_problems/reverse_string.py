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
    
def reverse_str(stack, input_string):
    for i in range(len(input_string)):
        stack.push(input_string[i])
    
    rever_string = ""
    while not stack.is_empty():
        rever_string += stack.pop()
    
    return rever_string
    

stack = Stack()

input_string = "Mithu"
result = reverse_str(stack, input_string)
print (f"Reverse of the string is: {result}")