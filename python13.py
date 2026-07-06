# Practice Problem: Write a program to count the total number of digits in a given 
# integer using a while loop.
try:
    num = int(input("Provide number:"))
    num_of_digits = 0
    while num > 0:
        num = num // 10
        num_of_digits += 1
    print(f"Number of digits: {num_of_digits}")
except ValueError:
    print('Provide valid number')