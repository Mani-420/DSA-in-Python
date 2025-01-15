import heapq

# Creating a heap
queue = [10, 20, 15, 30, 40]
heapq.heapify(queue)

# Find the 3 largest elements
max = heapq.nlargest(3, queue)
print("3 largest elements:", max)

# Find the 3 smallest elements
min = heapq.nsmallest(3, queue)
print("3 smallest elements:", min)