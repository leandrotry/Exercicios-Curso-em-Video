salario = float(input('digite o valor do salário de um funcionário: '))

aumento = salario * 0.15

salarioFinal = salario + aumento

print('O valor bruto do salário passou de R$ {:.2f} para R$ {:.2f} com 15% de aumento'.format(salario, salarioFinal))