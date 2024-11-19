# Reversing an Array---------------------------------------------------------

import array as arr

# Using reverse() method--------------------------

rever = arr.array("i", [1,2,3,4,5])
# rever = list(arr.array("i", [1,2,3,4,5]))
rever.reverse()
print(rever)


# Using slicing method--------------------------

sli = arr.array("i", [1,2,3,4,5])
# sli = list(arr.array("i", [1,2,3,4,5]))
reversed_arr = sli[::-1]
print(reversed_arr)


# Using for loop--------------------------

loop_method = arr.array("i", [1,2,3,4,5])
temp_arr = arr.array("i")

for i in range(len(loop_method)-1 , -1, -1):
    temp_arr.append(loop_method[i])

print(temp_arr)