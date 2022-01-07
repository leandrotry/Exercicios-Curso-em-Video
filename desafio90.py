dicionario = dict()

dicionario['nome'] = str(input('Digite o nome'))
dicionario['media'] = float(input('Digite a média'))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
else:
    dicionario['situacao'] = 'Reprovado'

for k, v in dicionario.items():
    print(f'{k} é igual a {v}')