def missing_numbers(array, total_numbers):
    expected_sum = total_numbers * (total_numbers + 1) // 2

    actual_sum = sum(array)
    return expected_sum - actual_sum


array = [1,2,4,5,6]
total_numbers = 6
result = missing_numbers(array, total_numbers)
print(f"The missing number is: {result}")