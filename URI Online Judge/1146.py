# -*- coding: utf-8 -*-

roda = True

while roda:
    n = int(input())

    if n == 0:
        roda = False
    else:
        for num in range(1, n + 1):
            if num == (n):
                print(num)
            else:
                print(num, end=' ')
