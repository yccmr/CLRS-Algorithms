# Implementation of doubly linked list

class DNode:
    def __init__(self, init_key, init_next=None, init_prev=None):
        self.key = init_key
        self.next = init_next
        self.prev = init_prev


class DLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def search(self, target_key):
        """ Return the index of the target_key, return -1 if it doesn't exist """
        index = 0
        current = self.head
        while current is not None:
            if current.key == target_key:
                return index
            current = current.next
            index += 1
        return -1

    def add(self, new_key):
        """ Add new_key at the head of the list """
        new_node = DNode(new_key)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, new_key):
        """ Append new_key to the end of the list """
        new_node = DNode(new_key)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def insert(self, new_key):
        """ Not implemented - the anticipated effect after the insertion is unknown, e.g. non-decreasing """
        pass

    def remove(self, target_key):
        """ Remove the target key from the list, do nothing if it doesn't exist """
        index = self.search(target_key)
        if index == -1:
            return

        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head.next.prev = None
            self.head = self.head.next
        elif index == self.length-1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:    # in the middle
            current = self.head
            for i in range(index):
                current = current.next
            current.next.prev = current.prev
            current.prev.next = current.next
        self.length -= 1

    def pop(self):
        """ Remove and return the last element from the list """
        if self.is_empty():
            return None

        removed_key = None
        if self.length == 1:
            removed_key = self.head.key
            self.head = None
            self.tail = None
        else:
            removed_key = self.tail.key
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.length -= 1
        return removed_key

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
            current = self.head
            while current.next is not None:
                result = result + str(current.key) + " -> "
                current = current.next
            result = result + str(current.key) + " :tail\n"

            result += "tail: "
            current = self.tail
            while current.prev is not None:
                result = result + str(current.key) + " -> "
                current = current.prev
            result = result + str(current.key) + " :head"
            return result


