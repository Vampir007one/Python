print("Введите первое число...")
a = int(input())
print("Введите второе число...")
b = int(input())
print("Введите третье число...")
c = int(input())

if(((a == b) and (a == c)) or ((b == a) and (b == c)) or ((c == a) and (c == b))):
    print("3 (все числа совпадают)")
else:
    if(((a == b) and (a != c)) or ((b == c) and (b != a)) or ((c == a) and (c != b))):
        print("2 (два числа совпадают)")
    else:
        print("0 (нет совпадений)")