# Implementation of queue

class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def enqueue(self, new):
        self.elements.append(new)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.elements.pop(0)

    def clear(self):
        self.elements = []     # or keep dequeue-ing

    def display(self):
        print(self)

    def __str__(self):
        if self.is_empty():
            return "(empty)"
        else:
            result = "head -> "
            for i in range(len(self.elements)):
                result = result + str(self.elements[i]) + " "
            result += "<- tail"
            return result


