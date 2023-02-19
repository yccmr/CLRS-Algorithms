# Implementation of max heap

def is_max_heap(arr):
    """ Return True if arr is a max heap, or False otherwise """
    pass


class MaxHeap:
    def __init__(self, arr):
        self.__max_heap = arr
        self.build_max_heap()

    def __get_left_child(self, root_index):
        """ Return the left child index given the root index """
        pass

    def __get_right_child(self, root_index):
        """ Return the right child index given the root index """
        pass

    def __get_parent(self, root_index):
        """ Return the parent index given the root index """
        pass

    def max_heapify(self):
        """ Change an almost max heap into a max heap """
        pass

    def build_max_heap(self):
        """ Build a heap from a random arr """
        pass

    def heap_sort(self):
        """ Sort into non-decreasing order """
        pass

    def is_in_heap(self, target):
        """ Return True if target is in the heap, or False otherwise """
        pass

    def find_max(self):
        """ Return the max element in the heap """
        pass

    def extract_max(self):
        """ Return and remove the max element from the heap """
        pass

    def insert(self, new):
        """ Insert the new data into an appropriate position s.t. the max heap structure is maintained """
        pass

    def delete(self, target):
        """ Delete target from the heap (if it exists) and maintain the heap structure """
        pass


