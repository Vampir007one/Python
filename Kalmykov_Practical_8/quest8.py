line = str(input("Введите строку: "))
first = line[:line.find('h')] 
second = line[line.find('h'):line.rfind('h') + 1]
third = line[line.rfind('h') + 1:]
line = first + second[::-1] + third
print("Новообразованная строка:",line)