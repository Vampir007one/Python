a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print("Полученные числа:",i)