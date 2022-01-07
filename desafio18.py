from math import cos, tan, sin, radians
angulo = float(input('digite o valor de um ângulo qualquer: '))

print('O valor do cosceno é {:.2f}, do tangente é {:.2f} e da seno é {:.2f}'.format(cos(radians(angulo)), tan(radians(angulo)), sin(radians(angulo))))