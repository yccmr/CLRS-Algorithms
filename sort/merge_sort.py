# Implementation of merge sort

def merge(l_sorted, r_sorted):
    """ Merge two sorted arrays into one """
    all_sorted = []
    i, j = 0, 0
    while i < len(l_sorted) and j < len(r_sorted):
        if l_sorted[i] < r_sorted[j]:
            all_sorted.append(l_sorted[i])
            i += 1
        else:
            all_sorted.append(r_sorted[j])
            j += 1
    all_sorted += l_sorted[i:]
    all_sorted += r_sorted[j:]
    return all_sorted


def merge_sort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a)//2
        l_sorted = merge_sort(a[:mid])
        r_sorted = merge_sort(a[mid:])
        return merge(l_sorted, r_sorted)


