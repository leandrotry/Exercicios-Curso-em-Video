lista = list()
total = 0


while continuar != 999:
    numero = float(input('Digite um valor'))
    if numero != 999:
        lista.append(numero)
    continuar = numero



print('Você digitou um total de {} valores'.format(len(lista)))
for i in range(0, len(lista)):
    total = total + lista[i]
print('A soma de todos os valores foi de {}'.format(total))
print(lista)
print()