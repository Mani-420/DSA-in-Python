# To find the smallest and largest element of an array------------------------

import array as arr

# Create an array
arr1 = arr.array('i', [10, 20, 5, 40, 15])

# Find the largest element
largest = max(arr1)

# Find the smallest element
smallest = min(arr1)

print(f"Largest element: {largest}") 
print(f"Smallest element: {smallest}")
