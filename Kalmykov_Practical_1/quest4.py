#Дано число n. С начала суток прошло n минут.
#Определите, сколько часов и минут будут показывать
#электронные часы в этот момент. Программа должна
#вывести два числа: количество часов (от 0 до 23) и
#количество минут (от 0 до 59). Учтите, что число n
#может быть больше, чем количество минут в сутках.
print("Введите любое целое число ...")
n = int(input())
hours = int(n/60)
minutes = int(n%60)
nextday = int(hours%24)

if(nextday < 10 and minutes < 10):
    print("0",nextday,": 0",minutes)
if(nextday < 10  and minutes >= 10):
    print("0",nextday,":",minutes)
if(nextday >= 10  and minutes >= 10 ):
    print(nextday,":",minutes)