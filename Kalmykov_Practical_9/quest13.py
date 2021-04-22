mass = [int(s) for s in input("Введите информацию: ").split()]
k = int(input("Введите индекс, который нужно удалить: "))
for i in range(k + 1, len(mass)):
    mass[i - 1] = mass[i]
mass.pop()
print(' '.join([str(i) for i in mass]))