#Practice Problem: Write a program to print a right-angled triangle pattern where 
# each row contains increasing numbers up to the row number
try:
    answer = int(input('Provide a number: '))
    line = ""
    for i in range(1, answer+1):
        line = line + (str(i) + " ") 
        print(line)
except ValueError:
    print('Provide valid number')

