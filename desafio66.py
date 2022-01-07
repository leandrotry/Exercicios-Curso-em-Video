numero = cont = total = 0

while True:
    numero = int(input('digite um valor (999 para o programa)'))
    if numero == 999:
        break
    cont += 1
    total += numero

print(f'O total de número inseridos foi de {cont} e o total da soma deles é de {total}')