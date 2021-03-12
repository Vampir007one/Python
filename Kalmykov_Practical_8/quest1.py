substr = " Подтекст для сообщения!"
inputMessage = (str(input("Введите текст: ")))
lineOld = inputMessage + substr 
lineNew = lineOld.replace(substr, "")
print("Старая строка:", lineOld)
print("Новая строка:", lineNew)