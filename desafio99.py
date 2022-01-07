def maior(* parm):
    lista = list()
    lista = parm
    tam = len(lista)
    m = 0
    for i in range(0, tam):
        if lista[i] > m:
            m = lista[i]
    print(m)



maior(2, 3, 4, 8, 1, 15, 92, 1, 2, 3, 4)