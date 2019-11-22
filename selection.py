def selection_sort(lista):
   for i in range(len(lista)):
       posicaoMin = i

       for j in range(i+1, len(lista)):
           if lista[posicaoMin] > lista[j]:
               posicaoMin = j
                
       temp = lista[i]
       lista[i] = lista[posicaoMin]
       lista[posicaoMin] = temp
   return lista
