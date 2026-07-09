# Practice Problem: Write a program to check if a number is an Armstrong number. 
# An Armstrong number (for a 3-digit number) is an integer such that the sum of the 
# cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).

int_answer = int(input("Provide a number : "))
str_answer = str(int_answer)

arm_num = 0

for i in range(len(str_answer)):
    arm_num += int((str_answer[i])) ** 3

if int_answer == arm_num:
    print('Yes')
else:
    print('No')