#Напишите программу, которая считывает целое число
#и выводит текст
#The next number for the number num1 is num2
#The previous number for the number num1 is num2
print("Введите любое целое число...")
number = int(input())
nexNumber = int(number + 1)
prevNumber = int(number - 1)
print("The next number for the number", number, "is", nexNumber)
print("The previous number for the number", number,  "is", prevNumber)
