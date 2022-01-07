altura = float(input('informe a altura da sua parede'))
largura = float(input('informe a largura da sua parede'))

area = largura * altura

tinta = area / 2

print('sua parede tem {}m² e para pinta-la, você precisará de {} litros de tinta'.format(area, tinta))