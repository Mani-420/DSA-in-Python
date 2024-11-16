# O( n^3 )
# Get every triplet of elements in array
# 3d scenarios with nested (3) loops


nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print(nums[i], nums[j], nums[k])