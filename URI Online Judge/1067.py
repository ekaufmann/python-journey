# -*- coding: utf-8 -*-

x = int(input())

if (1 <= x <= 1000):
    for i in range(x + 1):
        if (i % 2 == 1):
            print(i)
