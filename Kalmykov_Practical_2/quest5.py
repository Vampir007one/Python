#Составить программу вычисления функции у для
#нескольких значений x при некоторых постоянных значениях a и b. 
import math
from math import sqrt

print("Введите значение x...")
x = int(input())
a = 6
b = 10
y = abs((x**2) - (a**2)) + (9*x**3)/((b-x)**3) * math.sin(x/a)
print("Y:", y)

