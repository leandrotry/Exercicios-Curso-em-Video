numero = int(input('Digite um valor inteiro a ser convertido'))
opcao = int(input('''
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal
'''))

if opcao == 1:
    print('O valor {} para binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O valor {} para octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O valor {} para hexadecimal {}'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou um valor inválido. Tente novamente!')