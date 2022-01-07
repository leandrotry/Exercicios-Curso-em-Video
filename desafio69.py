menosvinte = somaidade = quanthomens = 0

while True:
    idade = int(input("Digite a idade"))
    if idade > 18:
        somaidade += 1
    while True:
        sexo = str(input("Digite o sexo")).upper().strip()
        if sexo == "M" or sexo == "F":
            if sexo == "F" and idade <= 20:
                menosvinte += 1
            elif sexo == "M":
                quanthomens += 1
            break
        else:
            print('Você digitou um sexo inválido!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar [S/N]')).upper().strip()[0]
    if continuar == "N":
        break


print(f'{somaidade} pessoas tem mais de 18 anos')
print(f'{quanthomens} quantidade de homens cadastrados')
print(f'{menosvinte} mulheres tem menos de 20 anos')
