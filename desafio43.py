altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilos: '))
imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print('Desnutrição')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Obeso!')
else:
    print('Obesidade mórbida')