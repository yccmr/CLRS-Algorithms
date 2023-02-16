# Implementation of selection sort

def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]


