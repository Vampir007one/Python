line = str(input("Введите строку: "))
firstWord = line[:line.find(' ')]
secondWord = line[line.find(' ') + 1:]
print("Новообразованная строка:",secondWord + ' ' + firstWord)