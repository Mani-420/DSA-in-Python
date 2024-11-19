# Rotating Array-------------------------------------------------

import array as arr

original = arr.array("i", [1,2,3,4,5,6,7])
shift = 3
temp_arr = arr.array("i")

for i in original:
    i = (i+shift) % len(original)
    temp_arr.append(original[i])

print(temp_arr)


# Leetcode Problem 189:
# class Solution(object):
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n  # Handle cases where k > n
#         # Reverse the entire array
#         nums.reverse()
#         # Reverse the first k elements
#         nums[:k] = reversed(nums[:k])
#         # Reverse the remaining n-k elements
#         nums[k:] = reversed(nums[k:])
        