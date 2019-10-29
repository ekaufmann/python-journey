# -*- coding: utf-8 -*-

valor = input().split()
valor = [float(i) for i in valor]
pi = 3.14159

print("TRIANGULO: %.3f" % ((valor[0] * valor[2]) / 2))
print("CIRCULO: %.3f" % ((valor[2] ** 2) * pi))
print("TRAPEZIO: %.3F" % (((valor[0] + valor[1]) * valor[2]) / 2))
print("QUADRADO: %.3f" % (valor[1] ** 2))
print("RETANGULO: %.3f" % (valor[0] * valor[1]))
