# -*- coding: utf-8 -*-

def Finaliza():
    while True:
        print('novo calculo (1-sim 2-nao)')
        opcao = int(input())
        if opcao == 2:
            return False
        elif opcao == 1:
            return True


notas = []
roda = True

while roda:
    n = float(input())

    if n < 0 or n > 10:
        print('nota invalida')
    else:
        if len(notas) < 2:
            notas += [n]
        
        if len(notas) == 2:
            print('media = %.2f' % ((notas[0] + notas[1]) / len(notas)))
            roda = Finaliza()
            if roda:
                notas = []
