termo = int(input('Digite o primeiro termo da sua Progressão aritmética'))
razao = int(input('Digite a razão na qual a progressão seguirá'))
decimo = termo + (10 - 1 ) * razao
i = 0
lista = []
for c in range(termo, decimo + razao, razao):
    lista.append(c)

print(lista[0:10])

