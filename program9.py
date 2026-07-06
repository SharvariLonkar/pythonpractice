# Practice Problem: Given a Python list, use a loop to print only the elements that 
# are located at odd index positions (index 1, 3, 5, etc.).


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0

while i < len(my_list):
    print(my_list[i])
    i += 2
