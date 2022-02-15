# max = 0
# i = 0
# max_i = 0
# a = int(input('Enter a Number (zero to quit): '))
# while a != 0:
#     if a > max:
#         max = a
#         max_i = i
#     a = int(input('Enter a Number (zero to quit): '))
#     i += 1
# print('Maximum:',max)
# print(max_i)

max = 0
i = 0
max_i = 0
a = int(input())
while a != 0:
    if a > max:
        max = a
        max_i = i
    a = int(input())
    i += 1
print(max_i)