lista_peso = list()

for c in range(0, 5):
    peso = float(input('Digite o peso a ser inserido na lista'))
    lista_peso.append(peso)
print('O maior peso lido foi {}Kg'.format(max(lista_peso, key= int)))
print('O menor peso lido foi {}Kg'.format(min(lista_peso, key= int)))