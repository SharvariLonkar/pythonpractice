# Practice Problem: Write a program that takes an integer n and prints the cube of
# every number from 1 to n in the format Current Number is : 1 and the cube is 1.

try:
    n = int(input('Provide a number: '))
    for i in range(1,n+1):
        print(f'Current number is : {i} and the cube is {i ** 3}')
except ValueError:
    print('Provide valid number')