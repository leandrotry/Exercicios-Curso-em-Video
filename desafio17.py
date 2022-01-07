from math import hypot

co = float(input('digite o valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjacente'))

print('o valor da hipotenusa é {}'.format(hypot(ca, co)))