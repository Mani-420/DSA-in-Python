# To remove the duplicate elements in an array------------------------

import array as arr

# Create an array
original = arr.array('i', [10, 20, 5, 40, 10, 25,5, 15])
temp_array = arr.array("i")

for num in original:
    if num not in temp_array:
        temp_array.append(num)

print(temp_array)
# original = temp_array

# Sorted Array--------------------------------

sorted_arr = sorted(temp_array)
print(sorted_arr)