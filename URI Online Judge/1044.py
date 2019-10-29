# -*- coding: utf-8 -*-

def Maior(x, y):
    if x < y:
        return y, x
    else:
        return x, y

a, b = map(int, input().strip().split())
a, b = Maior(a, b)

if (a % b == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
