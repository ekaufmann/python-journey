# -*- coding: utf-8 -*-

n = int(input())

if n > 1 and n < 1000:
    for num in range(1, n + 1):
        print(num, num ** 2, num ** 3)
        print(num, (num ** 2) + 1, (num ** 3) + 1)
