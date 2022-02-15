num = 0
a = int(input('Enter a Number (zero to quit): '))
while a != 0:
    if a % 2 == 0:
        num += 1
    a = int(input('Enter a Number (zero to quit): '))
print('Number of Even Values:',num)