lista = list()
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para ser acidionado à lista na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]

print(lista)
print(f'O maior valor presente na lista é {maior} nas posições ', end='')
for c,v in enumerate(lista):
    if v == maior:
        print(f'{c}...', end='')
        print()

print(f'O menor valor presente na lista é {menor} nas posições ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}...', end='')