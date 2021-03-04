#Дано трехзначное число. 
#Найти число, полученное при перестановке второй и третьей цифр 
# заданного числа.

print("Введите трёх значное число...")
number = int(input())
firstChar = number // 100
MiddleChar = number // 10 % 10
lastChar = number % 10  
print("Новое число:", firstChar, lastChar, MiddleChar)