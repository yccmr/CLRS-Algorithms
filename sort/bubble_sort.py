# Implementation of bubble sort

def bubble_sort(a):
    """ Bubble sort a into non-decreasing order """
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


