# -*- coding: utf-8 -*-

salario = float(input())
rendas = [2000, 3000, 4500]
faixa = [0.08, 0.18, 0.28]

if (salario <= rendas[0]):
    print('Isento')
else:
    if (salario <= rendas[1]):
        salario -= rendas[0]
        print('R$ %.2f' % (salario * faixa[0]))
    elif (salario <= rendas[2]):
        resto = salario - rendas[1]
        salario -= resto + rendas[0]
        print('R$ %.2f' % ((salario * faixa[0]) + (resto * faixa[1])))
    else:
        resto1 = salario - rendas[2]
        resto = salario - resto1 - rendas[1]
        salario -= resto + resto1 + rendas[0]
        print('R$ %.2f' % ((salario * faixa[0]) + (resto1 * faixa[2]) + (resto * faixa[1])))
