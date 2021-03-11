maxNum = 0
maxIndex = -1
number = -1
length = 0
while number != 0:
    number = int(input("Введите число:"))
    if number > maxNum:
        maxNum = number
        maxIndex = length
    length += 1
    print("#",length-1,":",number)
print("Индекс макс.числа:",maxIndex, "Число:", maxNum)