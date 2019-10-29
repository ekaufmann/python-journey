# -*- coding: utf-8 -*-

listaOr = input().split()
listaNova = [int(i) for i in listaOr]

listaNova.sort()
print(*listaNova, sep="\n")
print()
print(*listaOr, sep="\n")
