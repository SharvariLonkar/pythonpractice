# Practice Problem: Write a program to use a loop to find the factorial 
# of a given number (e.g., 5!). The factorial of N is the product of all integers 
# from 1 to N.

try:
    answer = int(input("Provide a number: "))

    factorial = answer

    for i in range(answer-1,0,-1):
        factorial = factorial * i

    print(f"Factorial: {factorial}")
except ValueError:
    print('Provide valid number')