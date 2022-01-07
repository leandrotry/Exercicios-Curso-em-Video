from time import sleep

def contador(i, f, p):
    """
    contador:
    :param i: início
    :param f: fim
    :param p: passo
    :return:
    """

    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')




i = int(input('i'))
f = int(input('f'))
p = int(input('p'))

contador(i,f,p)


