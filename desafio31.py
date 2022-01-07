km = int(input('digite a distância da viagem: '))
if km <= 200:
    print('O valor do quilometro é de R$ 0,50 e o valor total da viagem é de R$ {:.2f}'.format(km * 0.5))
else:
    print('O valor do quilometro é de R$ 0,50 e o valor total da viagem é de R$ {:.2f}'.format(km * 0.45))