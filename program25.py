answer = int(input("Provide a number"))

base_length = answer * 2 - 1

for i in range(1,answer+1,1):
    print("* " * i)
for i in range(answer-1,0,-1):
    print("* " * i)
