def bubble_sort(lista):
    n = len(lista)
    while True:
        trocado = False
        for i in range(1, n):
            if lista[i-1] > lista[i]:
                lista[i-1], lista[i] = lista[i], lista[i-1]
                trocado = True
        n -= 1
        if not trocado:
            break
    return lista