number = int(input("Введите число: "))
sum = 0
for i in range(1, number + 1):
    sum += i ** 3
print("Сумма кубов:",sum)