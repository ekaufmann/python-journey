# -*- coding: utf-8 -*-

prod1 = input().split()
prod2 = input().split()

valor1 = int(prod1[1]) * float(prod1[2])
valor2 = int(prod2[1]) * float(prod2[2])

print("VALOR A PAGAR: R$ %.2f" % (valor1 + valor2))
