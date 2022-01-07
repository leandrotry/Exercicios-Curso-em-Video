import random, time

quantidade = int(input('Quantos jogos você deseja gerar?'))
lista = list()
print('-+' * 30)
print('Gerando Jogos...')
print('-+' * 20)
for i in range(0, quantidade):
    x = 0
    while x < 6:
        jogo = random.randint(1, 60)
        if jogo not in lista:
            lista.append(jogo)
            x += 1
        lista.sort()
    print(f'{i+1}º jogo = {lista} ')
    time.sleep(0.3)
    lista.clear()


