class MinStack:
    def __init__(self):
        self.stack = []  # Main stack
        self.min_stack = [] #Stack to store minimums
    
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if not self.stack:
            print("Stack is empty")
        popped_element = self.stack.pop()
        # If the popped element is the current minimum, pop it from the min stack
        if popped_element == self.min_stack[-1]:
            self.min_stack.pop()
    
    def get_min(self):
        if not self.min_stack:
            print("Stack is empty, no minimum")
        return self.min_stack[-1]  # The top of the min stack is the current minimum
    
    def top(self):
        if not self.stack:
            print("Stack is empty")
        return self.stack[-1]

def main():
    stack = MinStack()
    stack.push(70)
    stack.push(90)
    stack.push(5)
    stack.push(60)
    stack.push(40)
    stack.pop()

    print(f"The current stack is: {stack.stack}")
    print(f"The minimum stack value is: {stack.get_min()}")


if __name__ == "__main__":
    main()
