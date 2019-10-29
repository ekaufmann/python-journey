# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

PAR = IMPAR = POSITIVO = NEGATIVO = 0

for X in (A, B, C, D, E):
  if (X%2==0):
    PAR=PAR+1
  if (X%2!=0):
    IMPAR=IMPAR+1
  if (X>0):
    POSITIVO=POSITIVO+1
  if (X<0):
    NEGATIVO=NEGATIVO+1

print ("%d valor(es) par(es)" %PAR)
print ("%d valor(es) impar(es)" %IMPAR)
print ("%d valor(es) positivo(s)" %POSITIVO)
print ("%d valor(es) negativo(s)" %NEGATIVO)
