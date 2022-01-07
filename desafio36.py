print('-=-' *20)
print('Programa de concessão de empréstimo')
print('-=-' *20)
salario =  float(input('Informe o valor do seu salário'))
casa = float(input('Informe o valor da casa que deseja comprar'))
ano = int(input('Informe em quantos anos deseja pagar o investimento'))

tempo = ano * 12
prestacao = casa / tempo
if prestacao <= salario * 0.3:
    print('você pode comprar a casa. O valor das parcelas é de R$ {:.2f} divididas em {} meses'.format(prestacao, tempo))
else:
    porcentagem = (prestacao / salario) * 100
    print('Você não pode comprar a casa, pois o valor das prestações representa um total de {:.2f}% do seu salário enquanto o valor máximo aceito é de 30% sobre o salário mensal'.format(porcentagem))