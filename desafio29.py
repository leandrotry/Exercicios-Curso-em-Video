velocidade = int(input('digite a velocidade do veículo'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Dirija com cuidado')