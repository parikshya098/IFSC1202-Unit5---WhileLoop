max = 0
c = 1
a = int(input('Enter a Number (zero to quit): '))
while a != 0:
    if a > max:
        max = a
        c = 1
    elif a == max:
        c += 1
    a = int(input('Enter a Number (zero to quit): '))
print('Maximum:',max)    
print('Number of Occurences:',c)