from unidecode import unidecode
nome = input('digite o seu nome completo').strip()
busca = unidecode(nome.lower())


if 'silva' in busca:
    print('seu nome possui a palavra "silva".')
else:
    print('seu nome NÃO possui a palavra "silva".')