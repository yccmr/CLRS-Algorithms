# Implementation of singly linked list

class Node:
    def __init__(self, init_data, init_next=None):
        self.__data = init_data
        self.__next = init_next

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data

    def get_next(self):
        return self.__next

    def set_next(self, new_next):
        self.__next = new_next

    def __eq__(self, other):
        return self.__data == other.get_data()


class SLinkedList:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def is_empty(self):
        return self.__length == 0

    def length(self):
        return self.__length

    def search(self, target_node):
        """ Return the index of the target_node. Return -1 if it doesn't exist """
        pass

    def add(self, new_node):
        """ Add new_node at the head of the list """
        pass

    def append(self, new_node):
        """ Append new_node to the end of the list """
        pass

    def insert(self, new_node, index):
        """ Add new_node to the specified position of the list. If index >= length, append it at the end of the list """
        pass

    def remove(self, target_node):
        """ Remove the target node from the list, do nothing if it doesn't exist """
        pass

    def pop(self):
        """ Remove the last element from the list """
        pass

    def clear(self):
        pass

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "head: "
            current = self.__head
            while current.next is not None:
                result = result + str(current) + " -> "
                current = current.next
            result += str(current)
            return result

