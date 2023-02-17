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


class SLinkedList:
    def __init__(self, head=None):
        self.__head = head
        self.__length = 0

    def is_empty(self):
        return self.__length == 0

    def length(self):
        return self.__length

    def search(self, target_data):
        """ Return the index of the target_data, return -1 if it doesn't exist """
        index = 0
        current = self.__head
        while current is not None:
            if current.get_data() == target_data:
                return index
            current = current.get_next()
            index += 1
        return -1

    def add(self, new_data):
        """ Add new_data at the head of the list """
        new_node = Node(new_data)
        if self.is_empty():
            self.__head = new_node
        else:
            new_node.set_next(self.__head)
            self.__head = new_node
        self.__length += 1

    def append(self, new_data):
        """ Append new_data to the end of the list """
        new_node = Node(new_data)
        if self.is_empty():
            self.__head = new_node
        else:
            current = self.__head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.__length += 1

    def remove(self, target_data):
        """ Remove the target data from the list, do nothing if it doesn't exist """
        index = self.search(target_data)
        if index == -1:
            return
        elif index == 0:
            removed = self.__head
            self.__head = self.__head.get_next()
            # removed.set_next(None)     # avoid future use
            self.__length -= 1
        else:
            current = self.__head
            for i in range(index-1):
                current = current.get_next()
            removed = current.get_next()
            current.set_next(current.get_next().get_next())
            # removed.set_next(None)     # avoid future use
            self.__length -= 1

    def pop(self):
        """ Remove and return the last element from the list """
        if self.is_empty():
            return None
        elif self.__length == 1:
            removed_data = self.__head.get_data()
            self.__head = None
            self.__length -= 1
            return removed_data
        else:
            current = self.__head
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            removed_data = current.get_data()
            previous.set_next(None)     # avoid future use
            self.__length -= 1
            return removed_data

    def clear(self):
        while not self.is_empty():
            self.pop()

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "head: "
            current = self.__head
            while current.get_next() is not None:
                result = result + str(current.get_data()) + " -> "
                current = current.get_next()
            result += str(current.get_data())
            return result


