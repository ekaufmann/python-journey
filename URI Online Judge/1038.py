# -*- coding: utf-8 -*-

compra = input().split()
prods = {'1':['Cachorro Quente', 4], '2':['X-Salada', 4.5], '3':['X-Bacon', 5], '4':['Torrada simples', 2], '5':['Refrigerante', 1.5] }

for codigo in prods:
    if (compra[0] == codigo):
        print('Total: R$ %.2f' % (float(prods[codigo][1]) * int(compra[1])))
