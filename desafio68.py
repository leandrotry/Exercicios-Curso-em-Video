from random import randint

vitorias = 0
while True:
    escolha = int(input('Digite um valor')) #Usuário escolhe um número
    computador = randint(1, 10)             #Computador escolhe um número
    resultado = computador + escolha        #Soma do resultado
    resultado1 = resultado % 2              #Testa se é par
    while True:
        parimpar = str(input('Par ou impar [P/I]')).upper().strip()[0]
        if parimpar == "P" or parimpar == "I":
            break

    if resultado1 == 0 and parimpar == "P":
        print(f'Você venceu com o resultado par {resultado}')
        vitorias += 1  # Calcula a quantidades de vitorias seguidas
    elif resultado1 == 1 and parimpar == "I":
        print(f'Você venceu com o resultado impar {resultado}')
        vitorias += 1  # Calcula a quantidades de vitorias seguidas
    else:
        print(f'Perdeu {resultado}')
        print(f'você venceu {vitorias} vezes consecutivas')
        break