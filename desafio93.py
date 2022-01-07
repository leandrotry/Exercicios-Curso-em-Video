campeonato = dict()
jogo = list()
i = totgols = 0
campeonato['nome'] = str(input('Digite o nome do Jogador'))
campeonato['partidas'] = int(input('Digite a quantidade de partidas disputadas'))
partidas = campeonato['partidas']

for i in range(0,partidas):
    jogo.append(int(input(f'Digite a quantidade de gols da partida')))

campeonato['gols'] = jogo[:]
campeonato['total'] = sum(jogo)

print(f'O jogador cadastrado tem o nome {campeonato["nome"]} e jogou  {campeonato["partidas"]}')
for k, v in enumerate(campeonato['gols']):
    print(f'Na partida {k}, fez {v} gols')
print(f'Fazendo um total de {campeonato["total"]} gols')