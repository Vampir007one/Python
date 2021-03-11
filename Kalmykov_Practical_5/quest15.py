number = int(input("Введите число: "))
if number == 0:
    print(0)
else:
    fibPrev, fibNext = 0, 1
    n = 1
    while fibNext <= number:
        if fibNext == number:
            print("Ответ:",n)
            break
        fibPrev, fibNext = fibNext, fibPrev + fibNext
        n += 1
    else:
        print(-1)