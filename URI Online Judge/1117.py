notas = []

roda = True
while roda:
    n = float(input())

    if n > 10 or n < 0:
        print('nota invalida')
    else:
        notas.append(n)
    
    if len(notas) == 2:
        roda = False

print((notas[0] + notas[1]) / len(notas))
