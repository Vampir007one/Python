#while
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
x = int(input("Введите число X: "))
counter = 0
while counter <= b:
    counter += 1 
    if(counter <= b):
        summa = a + counter
        if(summa % 10 == x):
            print("Полученное число:",summa)
#for
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
x = int(input("Введите число X: "))
for i in range(a,b+1):
    if(i%10 == x):
        print("Полученное число", i)