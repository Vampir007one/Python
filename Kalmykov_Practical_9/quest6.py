indexMax = 0
mass = [int(i) for i in input("Введите информацию: ").split()]
for i in range(1, len(mass)):
    if mass[i] > mass[indexMax]:
        indexMax = i
print("Наибольшее значение: ",mass[indexMax], "Его индекс: " ,indexMax)