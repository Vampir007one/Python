previos = int(input("Введите число: "))
result = 0
while previos != 0:
    next = int(input("Введите число: "))
    if next != 0 and previos < next:
        result += 1
    previos = next
print("Результат:",result)