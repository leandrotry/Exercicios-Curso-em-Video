from random import randint
a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)
e = randint(0,9)
tupla = a, b, c, d, e
print(tupla)
print(f'o maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')