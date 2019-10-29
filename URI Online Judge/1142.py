# -*- coding: utf-8 -*-

n = int(input())

for num in range(1, (4 * n) + 1):
    if num % 4 == 0:
        print('PUM')
    else:
        print(num, end=' ')
