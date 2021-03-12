line = str(input("Введите строку: "))
space = ''
for i in range(len(line)):
    if i % 3 != 0:
        space = space + line[i]
print("Новообразованная строка:",space)