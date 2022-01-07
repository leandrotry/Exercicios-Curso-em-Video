from random import randint


def sorteia(* num):
    lista = list()
    i = 0
    while i < 5:
        numero = randint(0, 10)
        i += 1
        lista.append(numero)
    print(lista)
    return lista

def somapar(* valores):
    soma = 0
    tam = len(valores[0])
    for i in range(0, tam):
        if valores[0][i] % 2 == 0:
            soma += valores[0][i]
    print(soma)


somapar(sorteia())
