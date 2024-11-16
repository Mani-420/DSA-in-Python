import array as arr

# Basic Operations ----------------------------------------------

# Finding length----------------------
find_length = arr.array("i", [1,2,3,4,5])
print(len(find_length))


# Adding/Changing---------------------------------------------------

# Append
append1 = arr.array("i", [1,2,3,4,5])
append1.append(6)
print(append1)

# Changing
arrChange = arr.array("i", [1,2,3,4,5])
arrChange[1] = 7
print(arrChange)

# Extend
extend1 = arr.array("i", [1,2,3,4,5])
extend1.extend([6])
print(extend1)

# Insert
insert1 = arr.array("i", [1,2,3,4,5])
insert1.insert(2, 7)
print(insert1)

# Deleting-----------------------------------------------------------

delete1 = arr.array("i", [1,2,3,4,5])
delete1.pop()
delete1.pop(0)
delete1.remove(2)
print(delete1)

# Concatenation-----------------------------------------------------------

concate1 = arr.array("i", [1,2,3])
concate2 = arr.array("i", [4,5,6])
concate1 += concate2
print(concate1)


# Slicing-----------------------------------------------------------

slice = arr.array("i", [1,2,3,4,5,6])
print(slice[3:5])

# Slicing-----------------------------------------------------------

iterate = arr.array("i", [1,2,3,4,5,6])
for x in iterate:
    print(x)


iterate2 = arr.array("i", [1,2,3,4,5,6])
i = 0
while i < len(iterate2):
    print(iterate2[i])
    i += 1