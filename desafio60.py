c = int(input('Digite um número inteiro para receber seu valor fatorial: '))
total = 1
if c == 0:
    print(0)
elif c == 1:
    print(1)
else:
    while c > 0:
        print(' {} '.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        total= total * c
        c = c - 1

    print(total)
