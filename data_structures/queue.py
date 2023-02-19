# Implementation of queue

class Queue:
    def __init__(self):
        self.__elements = []

    def is_empty(self):
        return self.__elements == []

    def size(self):
        return len(self.__elements)

    def enqueue(self, new):
        self.__elements.append(new)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__elements.pop(0)

    def clear(self):
        self.__elements = []     # or keep dequeue-ing

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


