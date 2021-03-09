print("Введите первое число...")
a = int(input())
print("Введите второе число...")
b = int(input())
print("Введите третье число...")
c = int(input())
if((a < b) and (a < c)):
    print("Наименьшее число:", a )
else:
    if((b < a) and (b < c)):
        print("Наименьшее число:", b)
    else:
        if((c < a) and (c < b)):
            print("Наименьшее число:", c)
