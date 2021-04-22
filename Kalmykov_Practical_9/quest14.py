mass = [int(s) for s in input("Введите информацию: ").split()]
#Индекс и число
k, C = [int(s) for s in input("Введите индекс и число: ").split()]
mass.append(0)
for i in range(len(mass) - 1, k, -1):
    mass[i] = mass[i - 1]
mass[k] = C
print(' '.join([str(i) for i in mass]))