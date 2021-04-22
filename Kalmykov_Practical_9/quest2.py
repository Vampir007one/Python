mass=input("Введите информацию:")
massEdit=[int(mass) for mass in mass.split()]
for i in massEdit:
    if int(i)%2 == 0:
       print("Чётные элементы списка: ",i)