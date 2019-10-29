# -*- coding: utf-8 -*-

def Inverte(a, b):
    if a > b:
        aux = a
        a = b
        b = aux
    return a, b

n = int(input())
impares = []

while n != 0:
    soma = 0
    x, y = map(int, input().split())
    x, y = Inverte(x, y)

    for num in range(x + 1, y):
        if num % 2 == 1:
            soma += num
    impares.append(soma)
    n -= 1

for valor in impares:
    print(valor)
