# Practice Problem: Write a program to print a right-angled triangle pattern where 
# each row contains increasing numbers up to the row number
answer = int(input("Provide a number :"))

for i in range(1, answer + 1,2):
    print(str(i) + " ", end='')