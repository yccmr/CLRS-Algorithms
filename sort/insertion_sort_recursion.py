# Implementation of insertion sort using recursion

def insertion_sort_recursion(a, r):     # r: right boundary index of a
    if r == 0:
        return
    else:
        insertion_sort_recursion(a, r-1)
        target = a[r]
        j = r-1
        while j >= 0 and a[j] > target:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = target


