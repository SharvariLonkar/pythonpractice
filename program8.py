# Practice Problem: Given a list of numbers, use a loop to count how many times a 
# specific number (e.g., 10) appears.
try:
    target = int(input("Enter a number whose frequency you'd like to check in the list: "))

    list = [10, 20, 10, 30, 10, 40, 50]

    frequency = 0

    for item in list:
        if item == target:
            frequency += 1

    print(f"The number {target} appeared {frequency} times in the list")
except ValueError:
    print("provide valid input")