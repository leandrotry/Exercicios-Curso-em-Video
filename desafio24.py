cidade = input('digite o nome da sua cidade').strip().lower()

if cidade.find('santo') == 0:
    print('Sua cidade começa com a palavra "SANTO"')
else:
    print('Sua cidade não começa com a palavra "SANTO"')