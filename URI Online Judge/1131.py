# -*- coding: utf-8 -*-

def Finaliza():
    while True:
        print('Novo grenal (1-sim 2-nao)')
        opcao = int(input())
        if opcao == 1:
            return True
        elif opcao == 2:
            return False


gols = []
roda = True
resultados = [0, 0, 0, 0] # grenais, inter, gremio, empates

while roda:
    gols += list(map(int, input().split()))
    resultados[0] += 1

    if gols[0] == gols[1]: # empate
        resultados[3] += 1
    elif gols[0] > gols[1]: # vitória Inter
        resultados[1] += 1
    else: # vitória Grêmio
        resultados[2] += 1
    
    roda = Finaliza()
    if roda:
        gols = []

print('%d grenais\nInter:%d\nGremio:%d\nEmpates:%d' % (resultados[0], resultados[1], resultados[2], resultados[3]))

if resultados[1] > resultados[2]:
    print('Inter venceu mais')
elif resultados[2] > resultados[1]:
    print('Gremio venceu mais')
