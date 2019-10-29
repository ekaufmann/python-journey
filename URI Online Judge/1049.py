# -*- coding: utf-8 -*-

def Verifica(info, lista):
    for tipo in lista:
        if (info[1] == tipo):
            for tipo2 in lista[tipo]:
                if (info[2] == tipo2):
                    print(lista[tipo][tipo2])


vertebrado = {'ave':{'carnivoro':'aguia', 'onivoro':'pomba'}, 'mamifero':{'onivoro':'homem', 'herbivoro':'vaca'}}
invertebrado = {'inseto':{'hematofago':'pulga', 'herbivoro':'lagarta'}, 'anelideo':{'hematofago':'sanguessuga', 'onivoro':'minhoca'}}
infos = []

i = 0
while i < 3:
    entrada = input()
    infos.append(entrada)
    i += 1

if (infos[0] == 'vertebrado'):
    Verifica(infos, vertebrado)
else:
    Verifica(infos, invertebrado)
