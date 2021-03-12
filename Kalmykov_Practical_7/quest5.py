line = str(input("Введите строку: "))
if line.count('f') == 1:
    print("F встречается один раз:",line.find('f'))
elif line.count('f') >= 2:
    print("F встречается 2 и более раз:",line.find('f'), line.rfind('f'))