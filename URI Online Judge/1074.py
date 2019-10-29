# -*- coding: utf-8 -*-

n = int(input())
entradas = []

while n != 0:
    entradas.append(int(input()))
    n -= 1

for i in entradas:
    if i == 0:
        print('NULL')
    
    if i > 0:
        if i % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    
    if i < 0:
        if i % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
