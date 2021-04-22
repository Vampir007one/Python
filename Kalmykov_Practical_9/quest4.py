mass = [int(massEdit) for massEdit in input("Введите информацию: ").split()]
for massEdit in range(1, len(mass)):
    if mass[massEdit - 1] * mass[massEdit] > 0:
        print("Итог: ",mass[massEdit - 1], mass[massEdit])
        break