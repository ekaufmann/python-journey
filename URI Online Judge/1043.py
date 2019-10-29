# -*- coding: utf-8 -*-

dados = input().split()
a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

if (a < b + c) and (b < a + c) and (c < a + b):
  print("Perimetro = %.1f" % (a + b + c))
else:
  print("Area = %.1f" % (((a + b)* c) / 2))
