mass = [int(s) for s in input("Введите информацию: ").split()]
counter = 0
for i in range(len(mass)):
    for j in range(i + 1, len(mass)):
        if mass[i] == mass[j]:
            counter += 1
print("Кол-во совпадений: ",counter)