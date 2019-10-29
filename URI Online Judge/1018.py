# -*- coding: utf-8 -*-

N = int(input())
valor = [100, 50, 20, 10, 5, 2, 1]
notas = []

if 0 < N < 1000000:
    print(N)
    for i in range(len(valor)):
        notas.append(N // valor[i])
        N = N - (notas[i] * valor[i])

    for i in range(len(valor)):
        print("%d nota(s) de R$ %d,00" % (notas[i], valor[i]))
