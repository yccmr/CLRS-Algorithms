# Implementation of a queue

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ Add the item at the end of the tail """
        self.items.append(item)

    def dequeue(self):
        """ Remove and return the item at the head """
        return self.items.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, false otherwise """
        return self.items == []

    def size(self):
        """ Return the size of the queue """
        return len(self.items)

    def __str__(self):
        return str(self.items)

