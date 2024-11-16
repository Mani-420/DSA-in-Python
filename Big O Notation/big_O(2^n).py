# O(2^n) Polynomial Time ----------------------------------------
# Recursive Functions
# Fabonachi Series


# Recursion, tree height n, two branches
def recursion(i, nums):
    if i == len(nums):
        return 0
    branch1 = recursion(i + 1, nums)
    branch2 = recursion(i + 2, nums)

# c branches, where c is sometimes n.
def recursion(i, nums, c):
    if i == len(nums):
        return 0
    
    for j in range(i, i + c):
        branch = recursion(j + 1, nums)
