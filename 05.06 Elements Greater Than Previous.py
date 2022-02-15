c = 0
b = int(input('Enter a Number (zero to quit): '))
a = b
while b != 0:
    if b > a:
       c += 1
    a = b
    b = int(input('Enter a Number (zero to quit): '))
print('Number of Values Greater Than the Previous:',c)