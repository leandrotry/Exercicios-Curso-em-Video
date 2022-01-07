numero = int(input('Digite um valor que deseja ver a tabuada: '))
print('-*-' * 10)
for c in range(0, 11):
    print('{} X {} = {}'.format(numero, c, (numero * c)))
print('-*-' * 10)