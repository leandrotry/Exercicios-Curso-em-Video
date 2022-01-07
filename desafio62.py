escolha = "S"
while escolha == "S":
    termo = int(input('Digite o primeiro termo da sua Progressão aritmética'))
    razao = int(input('Digite a razão na qual a progressão seguirá'))
    c = 0
    verdade = True
    while c < 10:
        print(termo)
        termo = termo + razao
        c += 1

    while verdade == True:
        escolha = str(input('Digite "S" sim ou "N" não se você deseja inserir uma nova escolha?')).capitalize().strip()
        if escolha == "S" or escolha == "N":
            verdade = False
        else:
            print('Você escolheu uma oção inválida. Tente Novamente')
