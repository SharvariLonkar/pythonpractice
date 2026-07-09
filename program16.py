# Practice Problem: Write a program to check if a given number is a 
# palindrome. A palindrome number is a number that remains the same when its 
# digits are reversed (e.g., 121, 343).


answer = input('Provide a number: ')
str_answer = str(answer)
reversed_answer = ''

for i in range(len(str_answer)-1, -1, -1):
    reversed_answer += (str_answer[i])

if reversed_answer == str_answer:
    print('Is a palindrome')
else:
    print('Is not palindrome')
