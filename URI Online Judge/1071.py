# -*- coding: utf-8 -*-

n1 = int(input())
n2 = int(input())
impar = 0

for i in range(n2 + 1, n1):
    if i % 2 == 1:
        impar = impar + i

print(impar)
