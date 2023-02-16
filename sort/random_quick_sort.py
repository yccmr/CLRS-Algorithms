# Implementation of random quick sort

import random


def random_partition(a, l, r):
    """
    Partition a[l..r] based on the randomly chosen pivot

    Parameters:
        - l: left boundary (index) of a
        - r: right boundary (index) of a

    Returns: p such that a[l..p-1] <= a[p] and a[p+1..r] >= a[p]
    """

    random_i = random.randint(l, r)     # randomly select a pivot
    a[random_i], a[r] = a[r], a[random_i]

    pivot = a[r]
    i = l-1
    for j in range(l, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def random_quick_sort(a, l, r):
    if l < r:
        q = random_partition(a, l, r)
        random_quick_sort(a, l, q-1)
        random_quick_sort(a, q+1, r)


