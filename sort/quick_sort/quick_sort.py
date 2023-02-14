# Implementation of quick sort

def partition(a, l, r):
    """
    Partition a[l..r] based on the last element being the pivot

    Parameters:
    	- l: left boundary (index) of a
    	- r: right boundary (index) of a

    Returns: p such that a[l..p-1] <= a[p] and a[p+1..r] >= a[p]
    """

    pivot = a[r]      # set the last element as pivot
    i = l-1
    for j in range(l, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def quick_sort(a, l, r):
    """ Quick sort a into non-decreasing order """

    if l < r:
        q = partition(a, l, r)
        quick_sort(a, l, q-1)
        quick_sort(a, q+1, r)


