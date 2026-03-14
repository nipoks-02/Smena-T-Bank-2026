start, end = map(int, input().split())
a, b = 0, 1
res = []

while a <= end:
    if a >= start:
        res.append(a)
    a, b = b, a + b
if res:
    print(*res)
else:
    print("В заданном диапазоне нет чисел Фибоначчи")
