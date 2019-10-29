# -*- coding: utf-8 -*-

def media(nota, peso):
    soma = 0
    for ind in range(len(notas)):
        soma += nota[ind] * peso[ind]
    return (soma / 10)

notas = list(map(float, input().strip().split()))
pesos = [2, 3, 4, 1]
media1 = media(notas, pesos)

print('Media: %.1f' % media1)
if (media1 < 5.0):
    print('Aluno reprovado.')
elif ((media1 >= 5.0) and (media1 <= 6.9)):
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame:', exame)
    media1 = (exame + media1) / 2
    if (media1 >= 5):
        print('Aluno aprovado.\nMedia final: %.1f' % media1)
    else:
        print('Aluno reprovado.')
else:
    print('Aluno aprovado.')
