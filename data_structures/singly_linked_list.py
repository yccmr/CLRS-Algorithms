# Implementation of singly linked list

class SNode:
    def __init__(self, init_key, init_next=None):
        self.key = init_key
        self.next = init_next


class SLinkedList:
    def __init__(self, head=None):
        self.head = head
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
        new_node = SNode(new_key)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, new_key):
        """ Append new_key to the end of the list """
        new_node = SNode(new_key)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def insert(self, new_key):
        """ Not implemented - the anticipated effect after the insertion is unknown, e.g. non-decreasing """
        pass

    def remove(self, target_key):
        """ Remove the target key from the list, do nothing if it doesn't exist """
        index = self.search(target_key)
        if index == -1:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
        self.length -= 1

    def pop(self):
        """ Remove and return the last element from the list """
        if self.is_empty():
            return None

        removed_key = None
        if self.length == 1:
            removed_key = self.head.key
            self.head = None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            removed_key = current.key
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
            result += str(current.key)
            return result


