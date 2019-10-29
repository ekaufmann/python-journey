# -*- coding: utf-8 -*-

xum, yum = input().split()
xum = float(xum)
yum = float(yum)
xdois,ydois = input().split()
xdois = float(xdois)
ydois = float(ydois)

distance = (((xdois - xum) ** 2) + ((ydois - yum) ** 2)) ** 0.5

print('%.4f' %distance)
