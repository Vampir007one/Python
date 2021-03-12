s = str(input("Введите строку: "))
s1 = str(input("Введите под строку s1: "))
s2 = str(input("Введите подстроку s2: "))
line = s + " " + s1 + " " + s2
if(s1 != s and len(s1) != 0):
    line = s + " " + s2 
if(len(s1) == 0 or s1 == s):
    line = s
print("Полученная строка:",line)