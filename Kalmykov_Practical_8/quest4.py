import re
str = str(input("Введите строку: "))
text = re.sub(r'\([^()]*\)', '', str)
print("Итог: ",text)