notas100 = notas50 = notas10 = notas1 = 0
valor = int(input('informe o valor que deseja sacar'))
while True:

    if valor > notas100:
        notas100 = valor // 100
        valor = valor - (notas100 * 100)
        print(f'Você sacou {notas100} notas de 100')

    if valor >= notas50:
        notas50 = valor // 50
        valor = valor - (notas50 * 50)
        print(f'Você sacou {notas50} notas de 50')

    if valor >= notas10:
        notas10 = valor // 10
        valor = valor - (notas10 * 10)
        print(f'Você sacou {notas10} notas de 10')

    if valor >= notas1:
        notas1 = valor // 1
        valor = valor // 1
        print(f'Você sacou {notas1} notas de notas 1')
        break





