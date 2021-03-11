cards = int(input("Введите количество карт: "))
card = 0
for i in range(1, cards + 1):
    card += i
for i in range(cards - 1):
    numTest = int(input("Введите число: "))
    card -= numTest
print("Номер потерянной карты: ",card)