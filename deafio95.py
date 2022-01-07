campeonato = dict()
jogo = list()
lista = list()
i = totgols = fim = 0
while True:
    campeonato['nome'] = str(input('Digite o nome do Jogador'))
    campeonato['partidas'] = int(input('Digite a quantidade de partidas disputadas'))
    partidas = campeonato['partidas']
    jogo.clear()
    for i in range(0,partidas):
        jogo.append(int(input(f'Digite a quantidade de gols da partida')))

    campeonato['gols'] = jogo[:]
    campeonato['total'] = sum(jogo)
    lista.append(campeonato.copy())

    while True:
        escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if escolha in 'SN':
            break
        print('Escolha inválida! Tente novamente')
    if escolha == 'N':
        break
print('cod ', end='')
for i in campeonato.keys():
    print(f'{i:<15}', end='')
print()
for k,v in enumerate(lista):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Deseja mostrar o dado de qual jogador? [999 finaliza]'))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! não existe jogador com o código {busca}')
    else:
        print(f' -- Levantamento do jogador {lista[busca]["nome"].upper()}')
        for k,v in enumerate(lista[busca]["gols"]):
            print(f'No jogo {k+1} fez {v} gols')
