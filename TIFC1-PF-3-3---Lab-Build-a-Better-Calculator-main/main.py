def addmultiplenumbers(numbers):
    # Returns the sum of all numbers in the list
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    # Returns the product of all numbers in the list
    result = 1
    for n in numbers:
        result *= n
    return result


def isitaninteger(num):
    # Checks if a number is an integer (e.g., 3.0 is considered an integer)
    return num == int(num)


def isiteven(num):
    # Checks if number is an even integer
    return isitaninteger(num) and int(num) % 2 == 0


def main():
    print("Simple Calculator")
    print("Enter numbers separated by spaces:")
    
    numbers = list(map(float, input().split()))

    print("\nChoose operation:")
    print("1 - Add")
    print("2 - Multiply")
    print("3 - Check if first number is even")
    print("4 - Check if first number is an integer")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Result:", addmultiplenumbers(numbers))
    elif choice == "2":
        print("Result:", multiplymultiplenumbers(numbers))
    elif choice == "3":
        print("Result:", isiteven(numbers[0]))
    elif choice == "4":
        print("Result:", isitaninteger(numbers[0]))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()