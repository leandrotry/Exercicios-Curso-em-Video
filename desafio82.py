lista = list()
listaPar = list()
listaImpar = list()
escolha = 'S'
while escolha != 'N':
    lista.append(int(input('Insira um valor na lista')))

    while True:
        escolha = str(input('Deseja continuar? [S/N]'))[0].strip().upper()

        if escolha not in 'SN':
            print(end='')
        else:
            break

for p in range(0, len(lista)):
    if lista[p] % 2 == 0:
        listaPar.append(lista[p])
    else:
        listaImpar.append(lista[p])
lista.sort()
listaPar.sort()
listaImpar.sort()
print(lista)
print(listaPar)
print(listaImpar)