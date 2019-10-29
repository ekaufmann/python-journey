# -*- coding: utf-8 -*-

n = int(input())
s = 0
r = 0
c = 0

while n != 0:
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    if (tipo == 'S'):
        s += int(quantia)
    elif (tipo == 'R'):
        r += int(quantia)
    else:
        c += int(quantia)
    n -= 1

total = r + c + s

print('Total: %d cobaias\nTotal de coelhos: %d\nTotal de ratos: %d\nTotal de sapos: %d' % (total, c, r, s))
print('Percentual de coelhos: {:.2f} %'.format((c / total) * 100))
print('Percentual de ratos: {:.2f} %'.format((r / total) * 100))
print('Percentual de sapos: {:.2f} %'.format((s / total) * 100))
