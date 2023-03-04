# Implementation of stack

class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def push(self, new):
        self.elements.append(new)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.elements.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elements[-1]

    def clear(self):
        self.elements = []    # or keep popping

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "bottom <- "
            for i in range(len(self.elements)):
                result = result + str(self.elements[i]) + " "
            return result



