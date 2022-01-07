def notas(*n, sit=False):
    """
    Verifica as notas e da a situação de um aluno por meio de um dicionário
    :param n: recebe a quantidade de notas informadas
    :param sit: (False por padrão) se True, informa a situação do aluno
    :return: retorna o dicionário
    """
    total = media = 0
    mostrar = dict()
    for i in enumerate(n):
        total += i[1]
    media = total / len(n)
    mostrar['Total'] = len(n)
    mostrar['Maior'] = max(n)
    mostrar['Menor'] = min(n)
    mostrar['Média'] = media

    if sit:
        if media < 5:
            mostrar['Situação'] = 'Ruim'
        elif media >= 5 and media < 7:
            mostrar['Situação'] = 'Média'
        else:
            mostrar['Situação'] = 'Boa'
    return mostrar




resp = notas(7,7,7,7)

print(resp)
help(notas)