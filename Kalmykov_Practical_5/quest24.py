zeroes = 0
repeat = int(input("Сколько раз выполнить программу: "))
for i in range(repeat):
    number = int(input("Введите число: "))
    if  number == 0:
        zeroes += 1
print("Количество нулей:",zeroes)