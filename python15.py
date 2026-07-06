# Practice Problem: Write a program to find the largest and smallest digit within a 
# given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

try:
    num = int(input('Provide number :'))
    strnum = str(num)

    greatest_number = 0
    smallest_number = 9
    for i in range(len(strnum)):
        if int(strnum[i]) > greatest_number:
            greatest_number = int(strnum[i])
        if int(strnum[i]) < smallest_number:
            smallest_number = int(strnum[i])
    print(f"Greatest number : {greatest_number} \nSmallest number : {smallest_number}")
    
except ValueError:
    print('Provide valid number')