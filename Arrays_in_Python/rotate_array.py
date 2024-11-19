# Rotating Array-------------------------------------------------

import array as arr

original = arr.array("i", [1,2,3,4,5,6,7])
shift = 3
temp_arr = arr.array("i")

for i in original:
    i = (i+shift) % len(original)
    temp_arr.append(original[i])

print(temp_arr)