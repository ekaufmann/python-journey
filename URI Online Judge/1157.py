# -*- coding: utf-8 -*-

n = int(input())
i = 1

while i <= n:
  if n % i == 0:
    print(i)
    i += 1
  else:
    i+= 1
