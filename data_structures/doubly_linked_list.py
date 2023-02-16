# Implementation of doubly linked list

class Node:
    def __init__(self, init_data, init_next=None, init_prev=None):
        self.__data = init_data
        self.__next = init_next
        self.__prev = init_prev

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data

    def get_next(self):
        return self.__next

    def set_next(self, new_next):
        self.__next = new_next

    def get_prev(self):
        return self.__prev

    def set_prev(self, new_prev):
        self.__prev = new_prev


class DLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def is_empty(self):
        return self.__length == 0

    def length(self):
        return self.__length

    def is_found(self):
        pass

    def insert(self, new_node, index):
        """ Add new_node to the specified position of the list. If index > length, add it at the end of the list """
        pass

    def remove(self, target_node):
        """ Remove the target node from the list, do nothing if it doesn't exist """
        pass

    def clear(self):
        pass

    def display(self):
        print(self)

    def __str__(self):
        pass


