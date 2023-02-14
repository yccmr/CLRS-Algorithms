# Implementation of insertion sort using recursion

def insertion_sort_recursion(a, r):
    """
    Insertion sort a in non-decreasing order using recursion

	Parameters:
    	- param a: an array of integers
    	- param r: right boundary index of a

    Returns: N/A
    """

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


