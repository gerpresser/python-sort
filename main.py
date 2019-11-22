import time
from generate_array import array_aleatorio, array_crescente, array_decrescente

# Sorts
from bubble import bubble_sort
from insertion import insertion_sort
from selection import selection_sort
from merge import merge_sort
from quick import quick_sort
from heap import heap_sort

if __name__ == "__main__":
    n = 30000

    rand_array = array_aleatorio(n)
    asc_array = array_crescente(n)
    desc_array = array_decrescente(n)
    
    # Bubble Sort
    print("Starting Bubble Sort - RAND")
    st = time.time()
    bubble_sort(rand_array)
    print('Bubble sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Bubble Sort - ASC")
    st = time.time()
    bubble_sort(asc_array)
    print('Bubble sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Bubble Sort - DESC")
    st = time.time()
    bubble_sort(desc_array)
    print('Bubble sort took %.3f seconds' % ((time.time() - st)))


    # --------------------------------------
    # Cleaning possible 'cached' data
    rand_array = array_aleatorio(n)
    asc_array = array_crescente(n)
    desc_array = array_decrescente(n)
    # --------------------------------------

    # Insertion Sort
    print("-----------------")
    print("Starting Insertion Sort - RAND")
    st = time.time()
    insertion_sort(rand_array)
    print('Insertion sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Insertion Sort - ASC")
    st = time.time()
    insertion_sort(asc_array)
    print('Insertion sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Insertion Sort - DESC")
    st = time.time()
    insertion_sort(desc_array)
    print('Insertion sort took %.3f seconds' % ((time.time() - st)))


    # --------------------------------------
    # Cleaning possible 'cached' data
    rand_array = array_aleatorio(n)
    asc_array = array_crescente(n)
    desc_array = array_decrescente(n)
    # --------------------------------------

    # Selection Sort
    print("-----------------")
    print("Starting Selection Sort - RAND")
    st = time.time()
    selection_sort(rand_array)
    print('Selection sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Selection Sort - ASC")
    st = time.time()
    selection_sort(asc_array)
    print('Selection sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Selection Sort - DESC")
    st = time.time()
    selection_sort(desc_array)
    print('Selection sort took %.3f seconds' % ((time.time() - st)))


    # --------------------------------------
    # Cleaning possible 'cached' data
    rand_array = array_aleatorio(n)
    asc_array = array_crescente(n)
    desc_array = array_decrescente(n)
    # --------------------------------------

    # Merge Sort
    print("-----------------")
    print("Starting Merge Sort - RAND")
    st = time.time()
    merge_sort(rand_array)
    print('Merge sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Merge Sort - ASC")
    st = time.time()
    merge_sort(asc_array)
    print('Merge sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Merge Sort - DESC")
    st = time.time()
    merge_sort(desc_array)
    print('Merge sort took %.3f seconds' % ((time.time() - st)))


    # --------------------------------------
    # Cleaning possible 'cached' data
    rand_array = array_aleatorio(n)
    asc_array = array_crescente(n)
    desc_array = array_decrescente(n)
    # --------------------------------------

    # Quick Sort
    print("-----------------")
    print("Starting Quick Sort - RAND")
    st = time.time()
    quick_sort(rand_array)
    print('Quick sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Quick Sort - ASC")
    st = time.time()
    quick_sort(asc_array)
    print('Quick sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Quick Sort - DESC")
    st = time.time()
    quick_sort(desc_array)
    print('Quick sort took %.3f seconds' % ((time.time() - st)))


     # --------------------------------------
    # Cleaning possible 'cached' data
    rand_array = array_aleatorio(n)
    asc_array = array_crescente(n)
    desc_array = array_decrescente(n)
    # --------------------------------------

    # Heap Sort
    print("-----------------")
    print("Starting Heap Sort - RAND")
    st = time.time()
    heap_sort(rand_array)
    print('Heap sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Heap Sort - ASC")
    st = time.time()
    heap_sort(asc_array)
    print('Heap sort took %.3f seconds' % ((time.time() - st)))

    print("")
    print("Starting Heap Sort - DESC")
    st = time.time()
    heap_sort(desc_array)
    print('Heap sort took %.3f seconds' % ((time.time() - st)))