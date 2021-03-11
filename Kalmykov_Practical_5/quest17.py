from math import sqrt
partialSum = 0
partialSumSquares = 0
n = 0
number = int(input("Введите число: "))
while number != 0:
    n += 1
    partialSum += number
    partialSumSquares += number ** 2
    number = int(input("Введите число: "))
answer = sqrt((partialSumSquares - partialSum ** 2 / n) / (n - 1))
print("Ответ:", answer)
