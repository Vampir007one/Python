P = int(input("Введите число P: "))
counter = 0
for i in range(1, 17+1):
    x = int(input("Введите число: "))
    if(x < P):
        counter += 1
if(counter == 0):
    print("Нет чисел меньше Р")
else:
    print("Чисел меньше P:", counter)