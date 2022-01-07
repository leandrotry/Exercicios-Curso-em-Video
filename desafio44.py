preco = float(input('digite o valor de um produto: '))

print('Digite "1" para pagar à vista no dinheiro ou cheque')
print('Digite "2" para pagar à vista no cartão')
print('Digite "3" para pagar em 2X no cartão sem júros')
print('Digite "4" para pagar em 3X ou mais no cartão (20%) de Júros. "Guanabara\'s Agiotágem" ')
escolha = int(input())
if escolha == 1:
    total = preco - (preco * 0.1)
    print(total)
elif escolha == 2:
    total = preco - (preco * 0.05)
    print(total)
elif escolha == 3:
    print(preco)
elif escolha == 4:
    total = preco + (preco * 0.2)
    print(total)