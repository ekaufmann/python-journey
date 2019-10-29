# -*- coding: utf-8 -*-

x, y = map(int, input().split())

if (x > 1 and x < 20) and (x < y and y < 100000):
    for num in range(1, y + 1):
        if num % x == 0:
            print(num)
        else:
            print(num, end=' ')        
