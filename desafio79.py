lista = list()
escolha = 'S'
while escolha != 'N':
    numero = int(input('Digite um valor para adicionar à lista'))
    if numero not in lista:
        lista.append(numero)
    else:
        print(f'O número {numero} já existe na lista, por isso, não será novamente adicionado')


    while True:
        escolha = str(input('Deseja adicionar um novo número [S/N]')).strip().upper()
        if escolha not in 'SN':
            print(end='')
        else:
            break
lista.sort()
print(lista)