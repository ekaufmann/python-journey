# -*- coding: utf-8 -*-

age = int(input())
year = age / 365
rest = age % 365
month = rest / 30
day = rest % 30

print('%d ano(s)\n'
      '%d mes(es)\n'
      '%d dia(s)' %(year, month, day))