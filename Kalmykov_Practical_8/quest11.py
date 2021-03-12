line = str(input("Введите строку: "))
firstLine = line[:line.find('h') + 1] 
secondLine = line[line.find('h') + 1:line.rfind('h')]
thirdLine = line[line.rfind('h'):]
line = firstLine + secondLine.replace('h', 'H') + thirdLine
print("Новообразованная строка:",line)