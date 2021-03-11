previos = -1
currentRepLength = 0
maxRepLength = 0
number = int(input("Введите число: "))
while number != 0:
    if previos == number:
        currentRepLength += 1
    else:
        previos = number
        maxRepLength = max(maxRepLength, currentRepLength)
        currentRepLength = 1
    number = int(input("Введите число: "))
maxRepLength = max(maxRepLength, currentRepLength)
print("Ответ: ", maxRepLength)