x = - 1 
number = 1
while x != 0:
    x = int(input("Введите число: "))
    if(x < 15 and x % 2 == 0 and x != 0):
        number *= x
        print("Произведение чётных чисел:",number)