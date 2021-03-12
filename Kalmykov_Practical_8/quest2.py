str = str(input("Введите строку: "))
strSplit = str.split()
count = 0
for i in range(len(strSplit)):
    if(strSplit[i] == strSplit[i].upper()):
        count += 1
print("Количество прописных слов:", count)
