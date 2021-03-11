counter = 0
count = 0
number = int(input("Введите число: "))
while number != 0:
    counter += number
    count += 1
    number = int(input("Введите число: "))
average = counter // count
print("Итог:", average)