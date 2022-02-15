max = 0
a = int(input('Enter a Number (zero to quit): '))
while a != 0:
    if a > max:
        max = a
    a = int(input('Enter a Number (zero to quit): '))
print('Maximum:',max)