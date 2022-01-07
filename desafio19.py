import random

lista = ['leandro', 'ariane', 'gustavo', 'jesus']

escolha = random.choice(lista)

print('O nome escolhido foi {}'.format(escolha.capitalize()))

random.shuffle(lista)

print(lista)