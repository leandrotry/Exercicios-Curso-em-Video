dado = list()
lista = list()
fim = 0
maior = menor = 0
while fim == 0:
    dado.append(str(input('Insira um nome')))
    dado.append(int(input('insira um peso')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    while True:
        escolha = str(input('Deseja continuar? [S/N]'))[0].upper().strip()
        if escolha in 'nN':
            fim = 1
            break
        elif escolha in 'sS':
            fim = 0
            break
        else:
            print('Você digitou um valor incorreto, tente novamente!')
print(f'A quantidade de pessoas cadastradas é de {len(lista)}')
print(f'A(s) pessoa(s) com maior peso ', end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'A(s) pessoa(s) com menor peso ', end=' ')
print()
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

print(f'A quantidade de registros é de {len(lista)}')



