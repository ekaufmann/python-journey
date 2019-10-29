# -*- coding: utf-8 -*-

valor = float(input())
intervalos = [0, 25, 50, 75, 100]

if ((valor >= intervalos[0]) and (valor <= intervalos[1])):
    print('Intervalo [0,25]')
elif ((valor > intervalos[1]) and (valor <= intervalos[2])):
    print('Intervalo (25,50]')
elif ((valor > intervalos[2]) and (valor <= intervalos[3])):
    print('Intervalo (50,75]')
elif ((valor > intervalos[3]) and (valor <= intervalos[4])):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
