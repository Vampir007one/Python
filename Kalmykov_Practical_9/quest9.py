mass = [int(i) for i in input("Введите информацию: ").split()]
for i in range(1, len(mass), 2):
    mass[i - 1], mass[i] = mass[i], mass[i - 1]
print("Итого: ",' '.join([str(i) for i in mass]))