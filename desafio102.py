def fatorial(n = 1, show=False):
    """

    :param n: (OPCIONAL) Recebe o valor que deseja ser fatorado
    :param show: (OPCIONAL) False por padrão. Indica se sera apresentado a conta completa
    :return: Retorna o valor calculado de "n"
    """

    f = 1
    if show:
        print(f'O fatorial de {n} é ')
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} ', end='')
            else:
                print(f'{c} x ', end='')

        print('= ', end='')

    for c in range(n, 0, -1):
        f *= c
    return f


print(fatorial(n = 6, show = True))