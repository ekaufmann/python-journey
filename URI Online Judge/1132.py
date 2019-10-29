# -*- coding: utf-8 -*-

x = int(input())
y = int(input())
x, y = min(x, y), max(x, y)

soma = 0

for num in range(x, y + 1):
    if num % 13 == 0:
        num += 1
    else:
        soma += num

print(soma)
