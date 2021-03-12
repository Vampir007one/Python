line = str(input("Введите строку: "))
if line.count('f') == 1:
    print("F встречается один раз:",-1)
elif line.count('f') < 1:
    print("F не встречается:",-2)
else:
    print("Второе вхождение F:",line.find('f', line.find('f') + 1))