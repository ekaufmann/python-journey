# -*- coding: utf-8 -*-

valor = input().split()
a = int(valor[0])
b = int(valor[1])
c = int(valor[2])

maiorAB = (a + b + abs(a - b)) / 2
maiorAB = (maiorAB + c + abs(maiorAB - c)) / 2

print("%d eh o maior" % maiorAB)
