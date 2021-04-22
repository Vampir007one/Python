mass = [int(s) for s in input("Введите информацию: ").split()]
for i in range(len(mass)):
    for j in range(len(mass)):
        if i != j and mass[i] == mass[j]:
            break
    else:
        print(mass[i], end=' ')
        