salario = float(input('Digite o valor do salário: '))
if salario >= 1250:
    print('O valor do salário teve aumento de 10% passando para {:.2f}'.format(salario + (salario * 0.1)))
else:
    print('O valor do salário teve aumento de 15>>>>>>% passando para {:.2f}'.format(salario + (salario * 0.15)))