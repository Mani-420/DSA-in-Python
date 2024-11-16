# O(n log n) Quasilinear Time ----------------------------------------
# Quick sort
# Merge sort
# Heap sort
# Very Slow. As the data increases it takes more and more time.


# HeapSort
import heapq
nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)     # O(n)
while nums:
    heapq.heappop(nums) # O(logn)

# MergeSort (and most built-in sorting functions)