
def leiaint(num):
    while True:
        try:
            teste = int(input(num))
        except (ValueError, TypeError):
            print(f'O tipo digitado é inválido. Tente novamente')
            continue
        except (KeyboardInterrupt):
            print('Parou sem digitar')
            return 0
        else:
            return teste
            break


def leiafloat(num):
    while True:
        try:
            teste = float(input(num).replace(',', '.'))
        except (ValueError, TypeError):
            print('O tipo informado não é Válido. Tente novamente')
        except (KeyboardInterrupt):
            print('Parou sem digitar')
            return 0
        else:
            return teste
            break



i = leiaint('Digite um valor')
f = leiafloat('Digite um valor')


print(f'Os valores digitados foram {i} e {f}')


