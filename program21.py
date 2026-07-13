# Practice Problem: Write a program to print a right-angled triangle pattern where each 
# row contains increasing numbers up to the row number
answer = int(input('Provide a number : '))

for i in range(answer,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print("")