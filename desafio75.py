a = int(input('digite o primeiro número'))
b = int(input('digite o segundo número'))
c = int(input('digite o terceiro número'))
d = int(input('digite o quarto número'))

tupla = a, b, c, d

print(f'O número 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) >= 1:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}')
else:
    print('O valor 3 não apareceu em nenhuma posição')
    print(f'Os valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
    