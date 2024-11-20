# The two-pointer technique is a problem-solving strategy commonly used in computer science and programming,
# especially in algorithms involving arrays, strings, or linked lists. It involves using two pointers (or indices)
# to traverse a data structure simultaneously, typically to achieve more efficient solutions to problems.

import array as arr

# Problem----------------------------------------
# Given a sorted array of integers, find the pairs of number that add up to a given target.

def finding_pair(arr1, target):

    left = 0
    right = len(arr1)-1
    pairs = []
    # result = arr.array("i")

    while left <= right:
        current_sum = arr1[left] + arr1[right]
        if current_sum == target:
            pairs.append((arr1[left], arr1[right]))
            left += 1
            right -= 1 
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return pairs

arr1 = arr.array("i", [1, 3, 4, 6, 7, 10])
target = 10

answer = finding_pair(arr1, target)
print(answer)

