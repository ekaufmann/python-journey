roda = True
while roda:
    soma = 0
    n, m = map(int,input().strip().split())
    n, m = min(n, m), max(n, m)

    if n <= 0 or m <= 0:
        roda = False
    else:
        for num in range(n, m + 1):
            print(num, end=' ')
            soma += num
        print('Sum=%s' % soma)
