from random import seed
from random import sample

def array_aleatorio(n):
    sequencia = [i for i in range(n)]
    aleatorio = sample(sequencia, n)
    return aleatorio

def array_crescente(n):
    sequencia = [i for i in range(n)]
    crescente = sample(sequencia, n)
    return crescente

def array_decrescente(n):
    sequencia = [i for i in range(n)]
    decrescente = sample(sequencia, n)
    return decrescente