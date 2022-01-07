def ajuda(opc):

    while True:
        opcao = input(str(opc).lower())
        msg = f'Mostrando o comando {opcao}'

        print(f'~' *(len(msg) + 2))
        print(f' {msg} ')
        print(f'~' * (len(msg) + 2))
        if opcao == 'fim':
            break
        else:
            help(opcao)



ajuda('Digite um comando que deseja verificar a ajuda: ')