# -*- coding: utf-8 -*-

nums = [i for i in range(1, 11)]

n = int(input())

if (2 < n < 1000):
    for valor in nums:
        print('%d x %d = %d' % (valor, n, valor * n))
