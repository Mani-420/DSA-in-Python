def fib(number):
    # Stop condition
    if (number == 0):
        return 0
    # Stop condition
    if (number == 1 or number == 2):
        return 1
    # Recursion function
    else:
        return (fib(number - 1) + fib(number - 2))


# Test Code
def main():
    number = int(input("Enter the number for the solution: "))
    print("Fibonacci series of 5 numbers is :",end=" ")
    # for loop to print the fibonacci series.
    for i in range(0,number): 
        print(fib(i),end=" ")
    

if __name__ == "__main__":
    main()