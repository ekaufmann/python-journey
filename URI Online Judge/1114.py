roda = True
senha = '2002'
while roda:
    entrada = input().strip()

    if entrada == senha:
        print('Acesso Permitido')
        roda = False
    else:
        print('Senha Invalida')
