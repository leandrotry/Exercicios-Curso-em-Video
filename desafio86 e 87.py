matriz = list()
z = 0
soma = soma3 = maior = 0

for l in range(0,3): #indica o valor da coluna
    for c in range(0,3): # indica o valor da linhaa
        valor = int(input(f'Digite o valor prara a posição [{l},{c}]'))
        matriz.append(valor)

for l in range(0,3):#indica o valor da coluna
    for c in range(0,3):# indica o valor da linha
        print(f'[ {matriz[z]} ]', end='')

        if c == 2:
            soma3 = soma3 + matriz[z]

        if l == 1:
            if matriz[z] > maior:
                maior = matriz[z]
        z += 1

    print() #pula uma linha
    
for s in range(0,len(matriz)):
    if matriz[s] % 2 == 0:
        soma = soma + matriz[s]

print(f'A soma dos valores pares é igual a {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'A soma do maior valor da segunda coluna é {maior}')