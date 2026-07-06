
try:
    num = int(input('write a number :'))
    reversed = ""
    while num > 0:
        reversed += str(num % 10)
        num = num // 10
        
    print(f"Reversed: {reversed}")
except ValueError:
    print('Provide valid number')