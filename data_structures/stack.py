# Implementation of stack

class Stack:
    def __init__(self):
        self.__elements = []

    def is_empty(self):
        return self.__elements == []

    def size(self):
        return len(self.__elements)	

    def push(self, new):
        self.__elements.append(new)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.__elements.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__elements[-1]

    def clear(self):
        self.__elements = []    # or keep popping

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "bottom <- "
            for i in range(len(self.__elements)):
                result = result + str(self.__elements[i]) + " "
            return result



