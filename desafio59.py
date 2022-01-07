from time import sleep
escolha = 0
v2 = int(input('digite um valor'))
v1 = int(input('digite outro valor'))
while escolha != 5:


    escolha = int(input("""Digite um valor que execute uma opração
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """))

    if escolha == 1:
        soma = v1 + v2
        print('A soma dos números {} + {} é {}'.format(v1, v2, soma))
    elif escolha == 2:
        produto = v1 * v2
        print('A multiplicação dos números {} x {} é {}'.format(v1, v2, produto))
    elif escolha == 3:
        if v1 > v2:
            maior = v1
            print('O maior valor entre {} e {} é  {}'.format(v1, v2, maior))
        elif v2 > v1:
            maior = v2
            print('O maior valor entre {} e {} é  {}'.format(v1, v2, maior))
        else:
            print('Os dois valores são iguais')
    elif escolha == 4:
        v2 = int(input('digite um valor'))
        v1 = int(input('digite outro valor'))
    elif escolha == 5:
        print('Você escolheu sair do programa!')
        sleep(2)
        print()
    else:
        print('Você escolheu um valor inválido. Tente novamente')

