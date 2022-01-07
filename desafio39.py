from datetime import date
nascimento = int(input('Informe seu ano de nascimento: '))

ano = date.today().year # obtem o ano atual
idade = ano - nascimento # função de cálculo de idade

if idade < 18:
    tempo = 18 - idade
    print('você ainda falta {} anos para se alistar ao serviço militar.'.format(tempo))
elif idade == 18:
    print('Já é hora de se alistar no seviço militar.')
else:
    tempo = idade - 18
    print('Já passou o tempo de alistamento a {} anos atrás '.format(tempo))