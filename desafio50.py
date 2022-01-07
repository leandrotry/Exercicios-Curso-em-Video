soma = 0
for c in range(0,6):
    numero = int(input('digite um valor a ser somado'))
    if numero % 2 == 0:
        soma += numero
print(soma)