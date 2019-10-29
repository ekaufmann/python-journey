# -*- coding: utf-8 -*-

def Reajuste(sal, per):
    reajuste = sal * per
    novoSal = sal + reajuste    
    percentual = int(per * 100)
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'.format(novoSal, reajuste, percentual))


valor = float(input())
p = 0

if (valor <= 400):
    p = 0.15
elif (valor <= 800):
    p = 0.12
elif (valor <= 1200):
    p = 0.1
elif (valor <= 2000):
    p = 0.07
else:
    p = 0.04

Reajuste(valor, p)
