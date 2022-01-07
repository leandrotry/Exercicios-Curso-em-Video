pessoa = dict()
lista = list()
fim = mediaIdade = totalIdade = 0
while True:
    pessoa['nome'] = str(input('Digite o nome da pessoa'))

    while True:
        pessoa['sexo'] = str(input('Digite o seu sexo')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('O sexo digitado não é válido')
    pessoa['idade'] = int(input('Digite a idade da peessoa'))
    lista.append(pessoa.copy())

    while True:
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Você digitou um valor incorreto. Tente novamente')

    if escolha == 'N':
        break

for i in range(0, len(lista)):
    totalIdade = totalIdade + lista[i]['idade']
mediaIdade = totalIdade / len(lista)
print(f'A quantidade de pessoas cadastradas foi de {len(lista)}')
print(f'A média de idade do grupo é de {mediaIdade}')
print(f'As pessoas sexo feminino são:')
for v in range(0, len(lista)):
    if lista[v]['sexo'] == 'F':
        print(lista[v]['nome'])
for i in range(0, len(lista)):
    if lista[i]['idade'] > mediaIdade:
        print(f'{lista[i]["nome"]} é maior que a média de idade do grupo, pois possui {lista[i]["idade"]} anos')