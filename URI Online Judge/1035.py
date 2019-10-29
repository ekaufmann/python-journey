# -*- coding: utf-8 -*-

valores = input().strip().split()

for i in range(len(valores)):
    valores[i] = int(valores[i])

a, b, c, d = valores[0], valores[1], valores[2], valores[3]

if ((b > c) and (d > a) and ((c + d) > (a + b)) and (c > 0) and (d > 0) and (a % 2 == 0)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
