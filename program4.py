# Practice Problem: Write a program that accepts a number from the user and 
# calculates the sum of all numbers from 1 up to that number.

try:
    num = int(input("Provide a number:"))
    sum = 0
    for i in range(1, num+1):
        sum += i
    print(f"Sum of all numbers from 1 to {num} is {sum}")

except ValueError:
    print('Provide valid number')