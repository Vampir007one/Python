maxFirst = int(input("Введите число: "))
maxSecond = int(input("Введите число: "))
if maxFirst < maxSecond:
    maxFirst, maxSecond = maxSecond, maxFirst
number = int(input("Введите число: "))
while number != 0:
    if number > maxFirst:
        maxSecond, maxFirst = maxFirst, number
    elif number > maxSecond:
        maxSecond = number
    number = int(input("Введите число: "))
print("Второе число по величине:",maxSecond)