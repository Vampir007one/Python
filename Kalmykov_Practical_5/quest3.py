print("Введите число... ")
number = int(input())
twoDegree = 2
degree = 1
while twoDegree <= number:
    twoDegree *= 2
    degree += 1
print("Полученная степень:",degree - 1, "| 2 ^",degree - 1 , "=",twoDegree // 2)