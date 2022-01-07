from statistics import mean
nome = list()
idade = list()
sexo = list()
m = list()

for c in range(0,4):
    nome.append(str(input('Digite o nome da pessoa')))
    idade.append(int(input('Digite a idade da pessoa')))
    sexo.append(str(input('Digite o sexo M ou F')).upper()[0])

for i, valor in enumerate(sexo):
    if sexo[i] == 'M':
        h = idade.index(max(idade))
for j, valor in enumerate(sexo):
    if sexo[j] == 'F':
        if idade[j] >= 20:
            m.append(idade[j])

print('A média de idade do grupo é {} anos'.format(mean(idade)))
print('O homem mais velho é {}'.format(nome[h]))
print('A quantidade de mulheres com mais de 20 anos é {}'.format(len(m)))






