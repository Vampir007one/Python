x = - 1
number = 1
while x != 0:
    x = int(input("Введите число: "))
    if(x % 7 == 0 and x != 0):
        number *= x
        print("Произведения чисел кратных 7:", number)