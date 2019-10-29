# -*- coding: utf-8 -*-

N = int(input())

segundos = N % 60
minutos = (N // 60) % 60
horas = ((N // 60) // 60) % 60

print("%d:%d:%d" % (horas, minutos, segundos))
