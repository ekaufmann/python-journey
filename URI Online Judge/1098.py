# -*- coding: utf-8 -*-

i = 0
j = 1

while i <= 2.0:
    if i == 0.0 or i == 1.0 or i > 1.8:
        print('I=%.0f J=%.0f' % (i, j))
    else:
        print('I=%.1f J=%.1f' % (i, j))

    if int(j - i) == 3:
        i += 0.2
        j = 1 + i
    else:
        j += 1
