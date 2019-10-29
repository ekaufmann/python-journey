# -*- coding: utf-8 -*-

tempos = input().split()
hInicial = int(tempos[0])
mInicial = int(tempos[1])
hFinal = int(tempos[2])
mFinal = int(tempos[3])

minutos = mFinal - mInicial
horas = hFinal - hInicial

if (horas < 0):
  horas += 24
if (minutos < 0):
  minutos += 60
  horas -= 1
if (horas == 0) and (minutos == 0):
  print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
  print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))
