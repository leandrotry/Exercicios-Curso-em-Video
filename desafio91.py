import random
jogadores = dict()
ranking = dict()
jogadores['player1'] = random.randint(1,6)
jogadores['player2'] = random.randint(1,6)
jogadores['player3'] = random.randint(1,6)
jogadores['player4'] = random.randint(1,6)

for k, v in jogadores.items():
    print(f'{k} lançou um dado com o número {v}')

for i in sorted(jogadores, key = jogadores.get, reverse = True):
    ranking[i] = (jogadores[i])

for j, p in ranking.items():
    print(f'O {j} obteve o {p} pontos')