# -*- coding: utf-8 -*-

def Q1(vx, vy):
    return (vx > 0 and vy > 0)

def Q2(vx, vy):
    return (vx < 0 and vy > 0)

def Q3(vx, vy):
    return (vx < 0 and vy < 0)

def Q4(vx, vy):
    return (vx > 0 and vy < 0)


x, y = map(float, input().strip().split())

if (x == y == 0):
    print('Origem')
elif (y == 0):
    print('Eixo X')
elif (x == 0):
    print('Eixo Y')
else:
    if Q1(x, y):
        print('Q1')
    elif Q2(x, y):
        print('Q2')
    elif Q3(x, y):
        print('Q3')
    else:
        print('Q4')
