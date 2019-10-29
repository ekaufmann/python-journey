# -*- coding: utf-8 -*-

def Media(lista):
    total = 0
    for valor in lista:
        total += valor
    return (total / len(lista))

nums = []
digitados = []

while len(digitados) < 6:
    entrada = float(input())
    digitados.append(entrada)
    if entrada > 0:
        nums.append(entrada)

print('%d valores positivos\n%.1f' % (len(nums), Media(nums)))
