# -*- coding: utf-8 -*-

a, b, c = map(float, input().split())
delta = (b ** 2) - 4 * a * c

if ((a == 0) or (delta < 0)):
    print('Impossivel calcular')
else:
    r1 = (-b + (delta ** (1/2))) / (2 * a)
    r2 = (-b - (delta ** (1/2))) / (2 * a)
    print('R1 = {:.5f}\nR2 = {:.5f}'.format(r1, r2))
