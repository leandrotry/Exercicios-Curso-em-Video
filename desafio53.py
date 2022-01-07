
from unidecode import unidecode
frase = input('Digite uma frase para testar se ela é um palíndromo').strip() #retira todos os espaços antes e depois
i = 0
lista = unidecode(frase.lower()) #retira qualquer caracter especial da frase
teste = lista.replace(' ', '') #retira os espaços da frase

lista2 = []

for c in range(len(teste)): #percorre a lista
    lista2.append(teste[i]) #insere cada item da lista na lista2
    i = i + 1               #muda o índice da lista

if lista2[:: -1] == lista2[:]: #Percorre lista 2 ao contrario e testa se é igual lista 2
    print('A frase é um Palíndromo, ou seja, pode ser lido ao contrário')
else:
    print('Não é um palíndromo')

print(lista2)
print(lista)