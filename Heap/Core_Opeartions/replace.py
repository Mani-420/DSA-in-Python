import heapq

# Create a min-heap
heap = [3, 5, 7, 10, 12]
heapq.heapify(heap)

print("Original heap:", heap)

# Replace the smallest element with a new value
replaced_value = heapq.heapreplace(heap, 6)

print("Replaced value:", replaced_value)
print("Updated heap:", heap)
