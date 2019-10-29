n = int(input().strip())

for rodada in range(n):
    x, y = map(int, input().strip().split())

    if y == 0:
        print('divisao impossivel')
    else:
        print(float(x / y))
