from datetime import date
pessoa = dict()
lista = list()

y = 0
z = 0

for c in range(0, 5):
    pessoa.clear()
    pessoa['nome'] = input('Digite um nome')
    ano_nascimeto = int(input('Digite o ano de nascimento'))
    pessoa['idade'] = date.today().year - ano_nascimeto

    lista.append(pessoa.copy())
for p in lista:
    if p["idade"] > 18:

        print(f'{p["nome"]} tem {p["idade"]} anos')
        y = y + 1
    else:

        print(f'{p["nome"]} tem {p["idade"]} anos')
        z = z + 1

print('A quantidade de pessoas maiores de idade são {}'.format(y))
print('A quantidade de pessoas menores de idade são {}'.format(z))



