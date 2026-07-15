# Practice Problem: Print a 5*5 square of stars where the middle is empty, leaving only the border.

answer = int(input("Provide a number"))

for i in range(1,answer+1,1):
    if i == 1 or i == answer:
        print("*" * answer)
    else:  
        print("*" + (" " * (answer-2)) + "*")
