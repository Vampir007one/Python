line = str(input("Введите число: "))
lastNum = len(line)-1
if(line[lastNum] > "2"):
    print("Да, число правда заканчивается на цифру больше 2")
else:
    print("Нет, последняя цифра не больше 2")
print("Количество цифр в данном числе:", len(line))