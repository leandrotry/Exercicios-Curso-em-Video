from time import sleep

print('{:=^40}'.format(' É ANO NOVO NESSE CARALHO! '))
print('Contagem regressiva pra acabar saporra!')
for c in range(10, 0, -1):
    print('{} segundos'.format(c))
    sleep(1)
print('=*=' * 15)
print('{: ^40}'.format('FELIZ ANO NOVO!'))
print('=*=' * 15)