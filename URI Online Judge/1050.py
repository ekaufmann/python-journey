# -*- coding: utf-8 -*-

def Verifica(num, lista):
    if (num in lista):
        print(lista[num])
    else:
        print('DDD nao cadastrado')
    

cidades = {61: 'Brasilia', 
            71: 'Salvador', 
            11: 'Sao Paulo', 
            21: 'Rio de Janeiro', 
            32: 'Juiz de Fora', 
            19: 'Campinas', 
            27: 'Vitoria', 
            31: 'Belo Horizonte'}

ddd = int(input())

Verifica(ddd, cidades)
