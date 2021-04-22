mass = [int(s) for s in input("Введите информацию: ").split()]
indexMin = 0
indexMax = 0
for i in range(1, len(mass)):
    if mass[i] > mass[indexMax]:
        indexMax = i
    if mass[i] < mass[indexMin]:
        indexMin = i
mass[indexMin], mass[indexMax] = mass[indexMax], mass[indexMin]
print(' '.join([str(i) for i in mass]))