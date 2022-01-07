from random import randint
computador = randint(0, 10)
acertou = False
tentativas = 0
while acertou != True:
    tentativas += 1
    numero = int(input('Digite um valor entre 0 e 10'))
    if numero < 0 or numero > 10:
        print('Você digitou um valor inválido! Tente novamente')
    elif numero == computador:
        print('Parabéns. Você acertou com {} tentativas'.format(tentativas))
        acertou = True
    else:
        print('Você errou! tente novamente')