def findSum(number):
    # Base case 
    if number == 0:
        return 0
    
    # Recursive case 
    return number + findSum(number - 1)


# Test Code
def main():
    number = int(input("Enter the number for the solution: "))
    print(findSum(number))


if __name__ == "__main__":
    main()