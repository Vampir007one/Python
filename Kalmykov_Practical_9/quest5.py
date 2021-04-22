mass = [int(massEdit) for massEdit in input("Введите информацию: ").split()]
countElem = 0
for massEdit in range(1, len(mass) - 1):
    # о боги, разве так можно писать?
    if mass[massEdit - 1] < mass[massEdit] > mass[massEdit + 1]:
        countElem += 1
print("Элементов больше соседей: ",countElem)