from collections import deque

# Create a deque
dq = deque()

# Add elements
dq.append(10)         # Add to the right end
dq.appendleft(20)     # Add to the left end
print("After additions:", dq)

# Remove elements
dq.pop()              # Remove from the right end
print("After popping right:", dq)
dq.popleft()          # Remove from the left end
print("After popping left:", dq)

# Add multiple elements
dq.extend([30, 40, 50])         # Add to the right end
dq.extendleft([60, 70, 80])     # Add to the left end
print("After extending:", dq)

# Rotate elements
dq.rotate(2)          # Rotate right by 2
print("After rotating right by 2:", dq)
dq.rotate(-3)         # Rotate left by 3
print("After rotating left by 3:", dq)

# Clear all elements
dq.clear()
print("After clearing:", dq)
