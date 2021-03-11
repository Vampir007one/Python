number = int(input("Введите число: "))
if number == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, number + 1):
        a, b = b, a + b
    print("Ответ:",b)