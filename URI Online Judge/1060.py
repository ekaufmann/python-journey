# -*- coding: utf-8 -*-

valores = []

i = 0
while i < 6:
    num = float(input())
    if (num > 0):
        valores.append(num)
    i += 1

print('%d valores positivos' % len(valores))
