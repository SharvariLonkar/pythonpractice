# Practice Problem: Write a program that counts the total number of vowels 
# and consonants in a given sentence, ignoring spaces and special characters.

answer = input("Say something:")

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
num_vowels = 0
num_consonants = 0

for i in range(len(answer)-1):
    if answer[i].lower() in vowels:
        num_vowels += 1
    elif answer[i].lower() in consonants:
        num_consonants += 1

print(f"Number of vowels: {num_vowels} \nNumber of consonants: {num_consonants}")
