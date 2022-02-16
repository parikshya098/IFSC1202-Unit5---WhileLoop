sum = 0
seq = 0
num = 0
max = 0
min = 0
c = 1
a = float(int(input('Enter a number (zero to quit): ')))

while a != 0 :
    if a > max:
        max = a
    elif a < min:
        min = a
    sum += a
    seq += a
    num += 1
    a = float(int(input('Enter a Number (zero to quit): ')))

z = (seq/num)

print('Count:',num)
print('Sum:',sum)
print ('Average:',z)
print('Minimum:',min)
print('Maximum:',max)