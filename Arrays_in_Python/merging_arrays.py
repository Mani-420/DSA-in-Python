# Merge 2 Sorted Arrays-------------------------------

import array as arr

# Create 2 array
arr1 = arr.array('i', [10, 20, 5, 40, 25, 15])
arr2 = arr.array('i', [100, 30, 4, 50, 25, 35])

# Merging and Sorting arrays----------------

new_arr = arr.array("i")
new_arr = arr1 + arr2
new_sorted_array = sorted(new_arr)

temp_array = arr.array("i")

# Removing Duplicates from arrays------------

for num in new_sorted_array:
    if num not in temp_array:
        temp_array.append(num)

print(temp_array)