import math
v1 = int(input('Digite o primeiro valor'))
v2 = int(input('Digite o segundo valor'))
v3 = int(input('Digite o terceiro valor'))

if (v1 > v2 and v1 > v3):
    print('o maior número é {}'.format(v1))
elif (v2 > v1 and v2 > v3):
    print('o maior número é {}'.format(v2))
elif (v3 > v1 and v3 > v2):
    print('o maior número é {}'.format(v3))

if (v1 < v2 and v1 < v3):
    print('o menor número é {}'.format(v1))
elif (v2 < v1 and v2 < v3):
    print('o menor número é {}'.format(v2))
elif (v3 < v1 and v3 < v2):
    print('o menor número é {}'.format(v3))