maxNum = 0
number = int(input("Введите число: "))
while number != 0:
    number = int(input("Введите число: "))
    if(number > maxNum):
        maxNum = number
print("Максимальное число в последовательности:", maxNum)
    
