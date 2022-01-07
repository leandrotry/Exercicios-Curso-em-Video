from statistics import mean
continuar = "S"

lista = list()

while continuar == "S":
    adicionar = True
    for c in range(0,5):
        numero = int(input('Digite um número que deseja adicionar'))
        lista.append(numero)
    print('O maior valor digitatdo foi {}'.format(max(lista)))
    print('O menor número inserido foi {}'.format(min(lista)))
    print('A média dos valores foi de {}'.format(mean(lista)))
    print('O número de itens inseridos na lista é de {} itens'.format(len(lista)))

    while adicionar:
        continuar = str(input('Deseja adicionar mais números?')).strip().capitalize()
        if continuar == "S" or continuar == "N":
            adicionar = False
        else:
            print('Você digitou um valor inválido. Tente novamente!')