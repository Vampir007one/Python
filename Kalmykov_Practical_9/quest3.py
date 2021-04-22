mass = [int(massEdit) for massEdit in input("Введите информацию: ").split()]
for massEdit in range(1, len(mass)):
    if mass[massEdit] > mass[massEdit - 1]:
        print("Элементы больше предыдущих: ",mass[massEdit])