def printFun(number):
    if (number < 1):
        return
    else:
        print(number, end=" ")
        printFun(number-1)
        print(number, end=" ")
        return


# Test Code
def main():
    number = int(input("Enter the number for palindrome: "))
    printFun(number)


if __name__ == "__main__":
    main()