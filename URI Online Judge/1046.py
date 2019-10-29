# -*- coding: utf-8 -*-

hInicio, hFinal = map(int, input().strip().split())

horas = hFinal - hInicio

if (horas < 0):
    horas += 24
if (horas == 0):
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU %d HORA(S)" % horas)
