lista = []
escolha = 'S'
while escolha != 'N':
    lista.append(int(input('Insira um valor na lista')))

    while True:
        escolha = str(input('Deseja continuar? [S/N]'))[0].strip().upper()

        if escolha not in 'SsNn':
            print(end='')
        else:
            break
print(f'A quantidade de valores digitados foi de {len(lista)}')
lista.sort(reverse=True)
print(f'Os valores da lista são {lista}')
if 5 in lista:
    print('O valor 5 se encontra na lista')
else:
    print('O valor 5 NÃO está na lista')