numero = int(input('digite um valor para mostrar sua tabuada'))
i = 1
contador = 0
print('-'*12)
while i < 12:
    resultado = numero * contador
    print('{} x {} = {}'.format(numero,contador, resultado))
    contador = contador +1
    i = i + 1
print('-'*12)