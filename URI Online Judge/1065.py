# -*- coding: utf-8 -*-

nums = []

i = 0
while i < 5:
    entrada = int(input())
    if (entrada % 2 == 0):
        nums.append(entrada)
    i += 1

print('{:d} valores pares'.format(len(nums)))
