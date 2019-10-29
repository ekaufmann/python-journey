# -*- coding: utf-8 -*-

def verifica(t):
    dias = int(t / 86400)
    aux = t % 86400
    horas = int(aux / 3600)
    aux = aux % 3600
    minutos = int(aux / 60)
    segundos = aux % 60
    
    print('%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)' % (dias, horas, minutos, segundos))

info = []
total = []

i = 0
while i < 4:
    entrada = input().upper()
    
    if 'DIA' in entrada:
        entrada = entrada.replace('DIA', '')
    else:
        entrada = entrada.replace(':', '')
    
    info += entrada.split()
    i += 1

for indice in range(len(info) // 2):
    total.append(int(info[indice + 4]) - int(info[indice]))

tempo = (total[0] * 86400) + (total[1] * 3600) + (total[2] * 60) + total[3]

verifica(tempo)
