maximum = 0
maximalNum = 0
number = -1
while number != 0:
    number = int(input("Введите число: "))
    if number > maximum:
        maximum, maximalNum = number, 1
    elif number == maximum:
        maximalNum += 1       
print("Количество элементов равных максимуму: ",maximalNum)