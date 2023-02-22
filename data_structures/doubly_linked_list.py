# Implementation of doubly linked list

class DNode:
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
    def __init__(self, head=None, tail=None):
        self.__head = head
        self.__tail = tail
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
        new_node = DNode(new_data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.set_next(self.__head)
            self.__head.set_prev(new_node)
            self.__head = new_node
        self.__length += 1

    def append(self, new_data):
        """ Append new_data to the end of the list """
        new_node = DNode(new_data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            new_node.set_prev(self.__tail)
            self.__tail = new_node
        self.__length += 1

    def insert(self, new_data):
        """ Not implemented - the anticipated effect after the insertion is unknown, e.g. non-decreasing """
        pass

    def remove(self, target_data):
        """ Remove the target data from the list, do nothing if it doesn't exist """
        index = self.search(target_data)
        if index == -1:
            return

        if self.__length == 1:
            self.__head = None
            self.__tail = None
        elif index == 0:
            self.__head.get_next().set_prev(None)
            self.__head = self.__head.get_next()
        elif index == self.__length-1:
            self.__tail.get_prev().set_next(None)
            self.__tail = self.__tail.get_prev()
        else:    # in the middle
            current = self.__head
            for i in range(index):
                current = current.get_next()
            current.get_next().set_prev(current.get_prev())
            current.get_prev().set_next(current.get_next())
        self.__length -= 1

    def pop(self):
        """ Remove and return the last element from the list """
        if self.is_empty():
            return None

        removed_data = None
        if self.__length == 1:
            removed_data = self.__head.get_data()
            self.__head = None
            self.__tail = None
        else:
            removed_data = self.__tail.get_data()
            self.__tail.get_prev().set_next(None)
            self.__tail = self.__tail.get_prev()
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
            result = result + str(current.get_data()) + " :tail\n"

            result += "tail: "
            current = self.__tail
            while current.get_prev() is not None:
                result = result + str(current.get_data()) + " -> "
                current = current.get_prev()
            result = result + str(current.get_data()) + " :head"
            return result


