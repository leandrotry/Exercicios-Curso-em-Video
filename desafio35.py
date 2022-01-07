a = float(input('digite o valor do primeiro lado do triângulo'))
b = float(input('digite o valor do segundo lado do triângulo'))
c = float(input('digite o valor do terceiro lado do triângulo'))

if a < b + c and b < a + c and c < a + b:
    print('A medida pode formar um triângulo')
else:
    print('As medidas não podem formar um triângulo')

