import random

numero = int(input('digite um número entre 0 e 5: '))
computador = random.randint(0, 5)
if numero < 0 or numero >= 6:
    print('você digitou um valor inválido')
elif numero == computador:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu!')

print('o valor escolhido pelo computador foi {}'.format(computador))

