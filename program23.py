#Practice Problem: Write a program to print a triangle pattern where each row consists of the 
# same letter, and the letter changes (increments) with each new row.
char = 96
for j in range(1,27):
    print((chr((char + j)).upper() + " ") * j)