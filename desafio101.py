>>>def voto(ano):
    from datetime import datev
    idade = date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos você não pode votar')
    elif (idade == 16 or idade < 18) or idade >= 65:
        print(f'Com {idade} anos o voto é opcional')
    else:
        print(f'Com {idade} anos o voto é obrigatório')


t = int(input('Digite o ano de seu nascimento'))
voto(t)