quantidade = float(input('informe o valor em reais que possui'))
dolares = quantidade / 5.72
print('com R$ {:.2f}, é possível comprar US$ {:.2f}'.format(quantidade, dolares))