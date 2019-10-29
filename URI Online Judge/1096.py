# -*- coding: utf-8 -*-

i = 1
j = 7

while i < 10:
    print('I=%d J=%d' % (i, j))
    
    j -= 1
    if j == 4:
        i += 2
        j = 7
