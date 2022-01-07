def jogador(nome, gols = 0):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato')

name = str(input('Digite o nome do jogador'))
points = str(input('informe a quantidade de gols feitos'))
jogador(name, points)