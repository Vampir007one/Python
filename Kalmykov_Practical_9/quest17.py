n, k = [int(s) for s in input("Введите кол-во кегель и бросков: ").split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input("Введите пару чисел: ").split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))