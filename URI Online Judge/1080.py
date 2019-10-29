# -*- coding: utf-8 -*-

nums = []
maior = 0

for indice in range(100):
    n = int(input())
    nums.append(n)
    if maior < n:
        maior = n

print(maior)
print(nums.index(maior) + 1)
