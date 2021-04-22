mass = input("Введите информацию: ").split()
for i in range(0, len(mass), 2):
    print("Элементы под чётными индексами: ", mass[i])
