# Implementation of stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """ Push the item on the top of the stack """
        self.items.append(item)

    def pop(self):
        """ Remove and return the item on the top """
        return self.items.pop()

    def peek(self):
        """ Display the element on the top """
        print(self.items[-1])

    def is_empty(self):
        """ Check if the stack is empty """
        return self.items == []

    def size(self):
        """ Return the size of the stack """
        return len(self.items)

    def __str__(self):
        return str(self.items)
