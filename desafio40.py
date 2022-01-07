nota1 = int(input('digite a primeira nota'))
nota2 = int(input('digite a segunda nota'))
media = (nota1 + nota2) / 2

if media < 5:
    print('Você foi reprovado com média {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você está de recuperação com média {}'.format(media))
else:
    print('você foi aprovado com média {}'.format(media))
