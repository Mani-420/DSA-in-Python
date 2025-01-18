import heapq

# Creating a heap
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)

# Replacing the smallest element (10) with 5
min = heapq.heapreplace(h1, 5)

print(min)
print(h1)

# Merging Heaps
h2 = [2, 4, 6, 8]

# Merging the lists
h3 = list(heapq.merge(h1, h2))
print("Merged heap:", h3)