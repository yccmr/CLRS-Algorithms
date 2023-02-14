# Implementation of insertion sort

def insertion_sort(a):
    """ Insertion sort a in non-decreasing order """
    
    for i in range(1, len(a)):
        target = a[i]
        j = i-1
        while j >= 0 and a[j] > target:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = target


