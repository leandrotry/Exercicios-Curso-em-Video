import datetime
ano = datetime.date.today().year
trabalhador = dict()
trabalhador['nome'] = str(input('Digite seu nome'))
nascimento = int(input('Digite seu ano de nascimento'))
trabalhador['idade'] = (ano - nascimento)
trabalhador['ctps'] = str(input('Digite o número da sua carteira de trabalho'))

while True:
    if len(trabalhador['ctps']) < 4:
        print('A carteira digitada é invalida. Digite novamente a CTPS com 4 dígitos')
        trabalhador['ctps'] = str(input('Digite o número da sua carteira de trabalho'))
    else:
        break

if trabalhador['ctps'] != '0000':
    trabalhador['contratacao'] = int(input('Digite o ano de sua contratação'))
    while True:
        if trabalhador['contratacao'] > ano:
            trabalhador['contratacao'] = int(input('O valor digitado não confere com o ano válido'))
        else:
            break
    trabalhador['salario'] = float(input('Digite o valor do seu salário'))
    trabalhador['aposentadoria'] = (trabalhador['contratacao'] + 35) - nascimento

for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')