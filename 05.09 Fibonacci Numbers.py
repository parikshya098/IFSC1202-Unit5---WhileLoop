n = int(input('Enter Fibonnaci Sequence Number: '))
fi1 = 0
fi2 = 1
if n < 1:
    print(0)
elif n == 1:
    print(1)
else:
    i = 2
    while i <= n:
        fi2, fi1 = fi1 + fi2, fi2
        i += 1
    print('Fibonacci Number:',fi2)