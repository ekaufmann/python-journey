# -*- coding: utf-8 -*-

opcoes = {1:'Alcool', 2:'Gasolina', 3:'Diesel', 4:False}
resultados = {1:0, 2:0, 3:0}
roda = True

while roda:
    escolha = int(input())

    if escolha in resultados:
        resultados[escolha] += 1
    elif escolha == 4:
        roda = opcoes[escolha]

print('MUITO OBRIGADO')
for resultado in resultados:
    print('%s: %d' % (opcoes[resultado], resultados[resultado]))
