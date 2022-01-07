tupla = ('Casa', 250, 'automovel', 750 )
print(type(tupla[0]))

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos] :.<30}', end=' ')
    else:
        print(f'R$ {tupla[pos]:.2f}')