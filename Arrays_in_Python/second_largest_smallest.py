# To find the second smallest and second largest element in an array------------------------

import array as arr

# Create an array
arr1 = arr.array('i', [10,10,10,11])

sorted_arr = sorted(arr1)

remove_duplicates = arr.array("i")

for num in sorted_arr:
    if num not in remove_duplicates:
        remove_duplicates.append(num)

print(remove_duplicates)

if len(remove_duplicates) < 2:
    second_largest = remove_duplicates[-1]
    print(f"Second Largest element: {second_largest}") 
    second_smallest = remove_duplicates[0]
    print(f"Second Smallest element: {second_smallest}")
else:
    # Find the largest element
    second_largest = remove_duplicates[-2]

    # Find the smallest element
    second_smallest = remove_duplicates[1]

    print(f"Second Largest element: {second_largest}") 
    print(f"Second Smallest element: {second_smallest}")

