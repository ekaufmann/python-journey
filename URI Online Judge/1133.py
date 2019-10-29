# -*- coding: utf-8 -*-

x = int(input())
y = int(input())
x, y = min(x, y), max(x, y)

for num in range(x + 1, y):
    if num % 5 == 2 or num % 5 == 3:
        print(num)
