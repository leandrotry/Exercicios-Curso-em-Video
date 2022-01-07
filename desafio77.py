tupla = ('palavra', 'teste', 'casa', 'fone', 'bone', 'rock', 'metal', 'slayer', 'counter-strike', 'celular', 'computador')

for posicao in range(0, len(tupla)):

    teste = tupla[posicao]

    print(f'na palavra "{tupla[posicao]}" temos as vogais ', end='')

    for palavra in range(0, len(teste)):
        if teste[palavra] == 'a':
            print(' a', end='')
        elif teste[palavra] == 'e':
            print(' e', end='')
        elif teste[palavra] == 'i':
            print(' i', end='')
        elif teste[palavra] == 'o':
            print(' o', end='')
        elif teste[palavra] == 'u':
            print(' u', end='')
    print()
