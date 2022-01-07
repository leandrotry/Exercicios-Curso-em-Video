lista = list()
fim = numero = 0

while fim == 0:

    nome = (input('Digite o nome:'))
    nota1 = (int(input('Digite a primeira nota')))
    nota2 = (int(input('Digite a primeira nota')))
    media = nota1 + nota2

    lista.append([nome, [nota1, nota2], media])

    while True:
        escolha = input('Deseja continuar? [S/N]')
        if escolha not in 'SsNn':
            print('Valor incorreto')
        if escolha in 'Ss':
            break
        elif escolha in 'Nn':
            fim = 1
            break

print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')

print('-' *30)

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    numero = int(input('Digite o código do aluno que você deseja ver a nota | 999 finaliza o programa'))
    if numero == 999:
        break
    if numero <= len(lista) - 1:
        print(f'Notas de  {lista[numero][0]} são {lista[numero][1]}')

