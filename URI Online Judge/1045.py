# -*- coding: utf-8 -*-

lados = input().split()

a = float(lados[0])
b = float(lados[1])
c = float(lados[2])
temp = 0

if (a < b):
  temp = a
  a = b
  b = temp

if (a < c):
  temp = a
  a = c
  c = temp

if (a >= (b + c)):
  print("NAO FORMA TRIANGULO")
else:
  if ((a ** 2) == (b ** 2) + (c ** 2)):
    print("TRIANGULO RETANGULO")
  elif ((a ** 2) > (b ** 2) + (c ** 2)):
    print("TRIANGULO OBTUSANGULO")
  elif ((a ** 2) < (b ** 2) + (c ** 2)):
    print("TRIANGULO ACUTANGULO")

  if (a == b == c):
    print("TRIANGULO EQUILATERO")
  elif (a == b) or (a == c) or (b == c):
    print("TRIANGULO ISOSCELES")
