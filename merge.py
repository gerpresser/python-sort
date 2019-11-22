def merge_sort(lista):
    if len(lista)>1:
        mid = len(lista)//2
        metadeEsquerda = lista[:mid]
        metadeDireita = lista[mid:]

        merge_sort(metadeEsquerda)
        merge_sort(metadeDireita)

        i=0
        j=0
        k=0

        while i < len(metadeEsquerda) and j < len(metadeDireita):
            if metadeEsquerda[i] < metadeDireita[j]:
                lista[k]=metadeEsquerda[i]
                i=i+1
            else:
                lista[k]=metadeDireita[j]
                j=j+1
            k=k+1

        while i < len(metadeEsquerda):
            lista[k]=metadeEsquerda[i]
            i=i+1
            k=k+1

        while j < len(metadeDireita):
            lista[k]=metadeDireita[j]
            j=j+1
            k=k+1

    return lista