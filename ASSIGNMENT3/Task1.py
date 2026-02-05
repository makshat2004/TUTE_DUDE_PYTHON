"""
Question:
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

"""

def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * calculate_factorial(number-1)

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is: {calculate_factorial(num)}")