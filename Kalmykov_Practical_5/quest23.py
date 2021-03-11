number = int(input("Введите число: "))
partialFactorial = 1
partialSum = 0
for i in range(1, number + 1):
    partialFactorial *= i
    partialSum += partialFactorial
print("Результат:",partialSum)