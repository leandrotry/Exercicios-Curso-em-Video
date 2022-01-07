import random

print('"0" para pedra')
print('"1" para papel')
print('"2" para tesoura')

lista = ['pedra', 'papel', 'tesoura']

computador = lista[random.randint(0,2)]

escolha_jogador = int(input('Escolha pedra, papel ou tesoura'))

jogador = lista[escolha_jogador]

if jogador == computador:
    print('empate')
elif jogador == 'pedra':
    if computador == 'papel':
        print('O computador venceu. Papel cobre pedra')
    else:
        print('Você venceu. Pedra elimina tesoura')
elif jogador == 'papel':
    if computador == 'tesoura':
        print('O computador venceu. Tesoura corta papel')
    else:
        print('Você venceu. Papel cobre pedra')
elif jogador == 'tesoura':
    if computador == 'pedra':
        print('Você perdeu. Pedra amassa tesoura!')
    else:
        print('Você ganhou. Tesoura Corta Papel')

print('-=' * 11)
print('você escolheu {} '.format(jogador.capitalize()))
print('O computador escolheu {}' .format(computador.capitalize()))
print('-=' * 11)
