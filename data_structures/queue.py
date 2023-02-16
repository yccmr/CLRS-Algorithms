# Implementation of queue

from student import STU


class Queue:
    def __init__(self):
        self.__elements = []

    def enqueue(self, new):
        self.__elements.append(new)

    def dequeue(self):
        return None if self.is_empty() else self.__elements.pop(0)

    def is_empty(self):
        return self.__elements == []

    def size(self):
        return len(self.__elements)

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "head -> "
            for i in range(len(self.__elements)):
                result = result + str(self.__elements[i]) + " "
            result += "<- tail"
            return result



