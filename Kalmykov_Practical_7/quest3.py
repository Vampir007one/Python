line = str(input("Введите строку: "))
print("Новая строка:",line[(len(line) + 1) // 2:] + line[:(len(line) + 1) // 2])