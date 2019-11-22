def quick_sort(lista):
    menor = []
    igual = []
    maior = []

    if len(lista) > 1:
        pivo = lista[0]
        for x in lista:
            if x < pivo:
                menor.append(x)
            elif x == pivo:
                igual.append(x)
            elif x > pivo:
                maior.append(x)
        return quick_sort(menor)+igual+quick_sort(maior)
    else:
        return lista