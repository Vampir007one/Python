#В школе решили набрать три новых математических
#класса. Так как занятия по математике у них проходят
#в одно и то же время, было решено выделить кабинет
#для каждого класса и купить в них новые парты. За
#каждой партой может сидеть не больше двух
#учеников. Известно количество учащихся в каждом из
#трёх классов. Сколько всего нужно закупить парт
#чтобы их хватило на всех учеников? Программа
#получает на вход три натуральных числа: количество
#учащихся в каждом из трех классов.

print("Введите количество учащихся в первом классе...")
quantityStudentFirstClass = int(input())
print("Введите количество учащихся во втором классе...")
quantityStudentSecondClass = int(input())
print("Введите количество учащихся в третьем классе...")
quantityStudentThirdClass = int(input())

#Первый кабинет
TwoStud_CabFirst = quantityStudentFirstClass//2
OneStud_CabFirst = quantityStudentFirstClass%2 
quantityTablesIn_FirstClass = int(TwoStud_CabFirst + OneStud_CabFirst)

#Второй кабинет
TwoStud_CabSecond = quantityStudentSecondClass//2
OneStud_CabSecond = quantityStudentSecondClass%2 
quantityTablesIn_SecondClass = int(TwoStud_CabSecond + OneStud_CabSecond)

#Третий кабинет
TwoStud_CabThird = quantityStudentThirdClass//2
OneStud_CabThird = quantityStudentThirdClass%2 
quantityTablesIn_ThirdClass = int(TwoStud_CabThird + OneStud_CabThird)

#Сумма парт
needTables = quantityTablesIn_FirstClass + quantityTablesIn_SecondClass + quantityTablesIn_ThirdClass

#Вывод по каждому кабинету
print("Количество парт для первого кабинета:", quantityTablesIn_FirstClass)
print("Количество парт для второго кабинета:", quantityTablesIn_SecondClass)
print("Количество парт для третьего кабинета:", quantityTablesIn_ThirdClass)

#Общий вывод для всех кабинетов
print("Всего нужно закупить парт:", needTables)
