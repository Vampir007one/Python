line = str(input("Введите строку: "))
line = line[:line.find('h')] + line[line.rfind('h') + 1:]
print("Новая строка:",line)