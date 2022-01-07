escolha = True
sexo = str(input('Digite o sexo de uma pessoa M ou F')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Você digitou uma tecla inválida, tente novamente.')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
