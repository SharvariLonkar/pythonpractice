# Practice Problem: Create a program that takes an integer and prints its multiplication 
# table from 1 to 10.

try:
    num = int(input("Provide a number:"))
    for i in range(1,11):
        print(i*num)

except ValueError:
    print('Provide valid number')

