# Practice Problem: Write a program that takes a string and reverses it using a for loop.
#  While Python’s [::-1] shortcut is famous, reversing a string manually is a classic way 
#  to understand how sequences are constructed

answer = input('write something:')

for i in range(len(answer)-1,-1,-1):
    print(answer[i], end='')
print("\n")