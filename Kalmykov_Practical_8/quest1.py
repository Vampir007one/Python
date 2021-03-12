# lineOld = "Старая строка: Hello, My name is Alexander!"
# lineNew = lineOld.replace("Старая строка: Hello, ", "")
# print(lineOld)
# print("Новая строка:",lineNew)

substr = " Подтекст для сообщения!"
inputMessage = (str(input("Введите текст: ")))
lineOld = inputMessage + substr 
lineNew = lineOld.replace(substr, "")
print("Старая строка:", lineOld)
print("Новая строка:", lineNew)