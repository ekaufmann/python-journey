# -*- coding: utf-8 -*-

i = 1
j = 7

while i < 10:
    print('I=%d J=%d' % (i, j))

    if j - i == 4:
        i += 2
        j += 4
    else:
        j -= 1
