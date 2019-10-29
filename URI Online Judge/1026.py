# -*- coding: utf-8 -*-

roda = True
while roda:
    try:
        x, y = map(int, input().split())
        print(x ^ y)
    except EOFError:
        break
