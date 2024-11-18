import array as arr


# Searching in array using "in" operator-------------------------------------

array1 = arr.array("i", [1,2,4,5,6,7])
element = 4

if element in array1:
    print(f"{element} is present in the array.")
else:
    print(f"{element} is not present in the array.")


# Searching in array using index() method-------------------------------------

index_mtd = arr.array("i", [1,2,4,5,6,7])
element = 4

try:
    index = array1.index(element)
    print(f"{element} is present at index {index}.")
except ValueError:
    print(f"{element} is not present in the array.")


# Searching in array using a loop-------------------------------------

array2 = [10, 20, 30, 40, 50]
element = 30

for i in range(len(array2)):
    if array2[i] == element:
        print(f"{element} is present at index {i}.")
        break
    
else:
    print(f"{element} is not present in the array.")
