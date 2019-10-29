roda = True
while roda:
    x, y = map(int, input().strip().split())

    if x < y:
        print('Crescente')
    elif x > y:
        print('Decrescente')
    else:
        roda = False
