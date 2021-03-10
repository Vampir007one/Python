import math
print("Введите x...")
x = int(input())
if(x <= math.pi):
    result = x + 2*math.sin(3*x)
if(x > math.pi):
    result = math.cos(x) + 2
print("Результат:", result)

