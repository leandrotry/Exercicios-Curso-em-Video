
total = maiorqmil = menor = cont = 0
barato = ' '

while True:
    nome = str(input("Digite o nome do produto"))
    valor = float(input("Digite o valor do produto"))
    total += valor
    cont += 1
    if valor > 1000:
        maiorqmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = nome

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Digite [S/N] se você deseja ou não continuar')).upper().strip()[0]
    if escolha == "N":
        break


print(f'O produto mais barato é {barato} custando {menor}')
print(f'A quantidade de produtos maiores que mil reais é {maiorqmil}')
print(f'O total da compra foi de {total}')




