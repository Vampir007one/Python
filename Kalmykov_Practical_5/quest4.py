print("Введите x...")
x = int(input())
print("Введите y...")
y = int(input())
day = 1
while x < y:
    x *= 1.1
    day += 1
print("День:", day)