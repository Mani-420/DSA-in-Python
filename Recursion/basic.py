def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)     


def main():
    number = int(input("Enter the number for factorial: "))
    result = factorial(number)
    print(f"The factorial of a number is: {result}")


if __name__ == "__main__":
    main()