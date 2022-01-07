while True:
    contagem = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    numero = int(input('Digite um valor entre 0 e 20: '))
    while True:
        if numero < 0 or numero > 20:
            numero = int(input('Tente Novamente. Digite um valor entre 0 e 20: '))
        else:
            break
    print(f'Você escolheu o número {contagem[numero]}')
    break