sequence = 0
number = 0
x = int(input('Enter a Number (zero to quit): '))
while x != 0:
    sequence += x
    number += 1
    x = int(input('Enter a Number (zero to quit): '))
a = (sequence/number)
print ('Average:',a)