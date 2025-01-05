def is_balanced(expression):
    stack = []  #Empty stack
    # Dictionary to map closing symbols
    matching_symbols = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        # If it's an opening symbol, push it onto the stack
        if char in "({[":
            stack.append(char)
        # If it's a closing symbol
        elif char in ")}]":
            # Check if the stack is empty or the top doesn't match
            if not stack or stack.pop() != matching_symbols[char]:
                return False
    
    # If stack is empty, symbols are balanced
    return len(stack) == 0

# Test the function
expression1 = "{[()]}"
expression2 = "{[(])}"

print(is_balanced(expression1))
print(is_balanced(expression2))