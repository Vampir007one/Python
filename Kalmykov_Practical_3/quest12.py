print("Введите N...")
N = int(input())
print("Введите M...")
M = int(input())
print("Введите x...")
x = int(input())
print("Введите y...")
y = int(input())

if(N > M):
    N, M = M, N
if(x >= N/2):
    x = N - x
if(y >= M/2):
    y = M - y
if(x < y):
    print("До бортика нужно проплыть:",x,"м")
else:
    print(print("До бортика нужно проплыть:",y,"м"))

