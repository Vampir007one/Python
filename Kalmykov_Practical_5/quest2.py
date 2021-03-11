print("Введите число не меньшее 2...")
number = int(input())
i = 2
while number % i != 0:
    i += 1
print("Наименьший делитель:",i)