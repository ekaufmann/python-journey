def quadrante(pontoX, pontoY):
    if pontoX > 0:
        if pontoY > 0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if pontoY > 0:
            print('segundo')
        else:
            print('terceiro')

roda = True
while roda:
    x, y = map(int, input().strip().split())

    if x == 0 or y == 0:
        roda = False
    else:
        quadrante(x, y)
