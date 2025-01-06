# Stock span is usually (how many times a value forced stack to pop + 1)

def calculate_span(prices):
    stack = []
    spans = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # If stack is empty:
        if not stack:
            spans[i] = i + 1
        else:
            # Else, span is the difference between current index and top of the stack
            spans[i] = i - stack[-1]
        
        # Push the current index onto the stack
        stack.append(i)
    
    return spans

# Example usage
prices = [100, 40, 50, 60, 40]
print("Stock Prices:", prices)
print("Stock Span:", calculate_span(prices))
