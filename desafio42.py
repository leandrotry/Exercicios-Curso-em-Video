import math
print('-=-=-' * 15)
print('Programa de construção do triângulo')
print('-=-=-' * 15)

a = float(input('Digite a medida do lado: '))
b = float(input('Digite a medida do lado: '))
c = float(input('Digite a medida do lado: '))

if a < b + c and b < a + c and c < a + b:
    print('A medida pode formar um: ')
    if a == b == c:
        print('Triângulo equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo isóceles')
    else:
        print('Triângulo escaleno')
else:
    print('A medida não pode formar um triângulo')