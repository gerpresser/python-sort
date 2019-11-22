def heap_sort(lista): 
    n = len(lista) 
  
    for i in range(n, -1, -1): 
        heap_handler(lista, n, i) 
  
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i]
        heap_handler(lista, i, 0)
    
    return lista

def heap_handler(lista, n, i): 
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and lista[i] < lista[l]: 
        maior = l 
  
    if r < n and lista[maior] < lista[r]: 
        maior = r 
  
    if maior != i: 
        lista[i],lista[maior] = lista[maior],lista[i]
  
        heap_handler(lista, n, maior)