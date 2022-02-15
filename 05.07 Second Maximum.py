max_2 = -1
a = int(input('Enter a Number (zero to quit): '))
max = 0
while a != 0:
    if a > max:
        max_2 = max
        max = a
    elif a > max_2:
        max_2 = a
    a = int(input('Enter a Number (zero to quit): '))
print(max_2)