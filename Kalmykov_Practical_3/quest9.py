print("Введите первое число (от 1 до 8)...")
num1 = int(input())
print("Введите второе число (от 1 до 8)...")
num2 = int(input())
print("Введите третье число (от 1 до 8)...")
num3 = int(input())
print("Введите четвёртое число (от 1 до 8)...")
num4 = int(input())
if(num1 >= 0 and num1 < 9):
    if(num2 >= 0 and num2 < 9):
        if(num3 >= 0 and num3 < 9):
            if(num4 >= 0 and num4 < 9):
                if( (abs(num1 - num2) == abs(num3 - num4)) or (num1 == num2 or num3 == num4) ): 
                    print("YES")
                else:
                    print("NO")
            else:
                print("Второе число не соответствует условию, повторите ввод заново")
        else:
            print("Третье число не соответствует условию, повторите ввод заново")
    else:
        print("Второе число не соответствует условию, повторите ввод заново")
else:
    print("Первое число не соответствует условию, повторите ввод заново")
