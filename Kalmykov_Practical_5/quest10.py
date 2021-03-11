chet = -1
number = -1
while number != 0:
    number = int(input("Введите число: "))
    if number % 2 == 0:
        chet += 1
print("Количество чётных элементов:",chet)