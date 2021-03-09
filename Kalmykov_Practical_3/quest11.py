print("Введите число n...")
n = int(input())
print("Введите число m...")
m = int(input())
print("Введите число k...")
k = int(input())

if(k < n * m and ((k % n == 0) or (k % m == 0))):
    print("Yes")
else:
    print("No")
