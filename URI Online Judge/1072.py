# -*- coding: utf-8 -*-

n = int(input())
lista = []

for i in range(n):
  numero = int(input())
  if ((numero < (10 ** 7)) and (numero > (-10 ** 7))):
    lista.append(numero)

i = 0
dentro = 0
fora = 0

while (i < len(lista)):
  if (lista[i] in range(10, 20)):
    dentro += 1
  else:
    fora += 1

  i += 1

print("%d in\n"
      "%d out" % (dentro, fora))
