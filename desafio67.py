resultado = 0
while True:
    numero = int(input('digite um número inteiro'))
    i = 0
    if numero < 0:
        break
    while i < 11:
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
        i += 1
 