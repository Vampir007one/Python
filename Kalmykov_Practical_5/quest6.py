counter = 0
number = int(input("Введите число: "))
while number != 0:
    counter += number
    number = int(input("Введите число: "))
print("Итог:", counter)