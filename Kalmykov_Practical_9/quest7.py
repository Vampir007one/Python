height = [int(i) for i in input("Введите рост ученика: ").split()]
X = int(input("Введите рост Пети: "))
position = 0
while position < len(height) and height[position] >= X:
    position += 1
print("Позиция Пети в шеренге", position + 1)