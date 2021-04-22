mass = [int(i) for i in input("Введите информацию:").split()]
countElements = 1
for i in range(0, len(mass) - 1):
    if mass[i] != mass[i + 1]:
        countElements += 1
print("Различных элементов в массиве:", countElements)